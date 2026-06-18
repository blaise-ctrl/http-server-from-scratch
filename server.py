import socket
import threading
import json
import time
import mimetypes
from datetime import datetime

request_count = 0
server_start_time = time.time()
request_count_lock = threading.Lock()

log_lock=threading.Lock()
HOST = "127.0.0.1"
PORT = 4221

def log_request(method,path,status_code,elapsed_ms):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"{timestamp} "
        f"{method} "
        f"{path} "
        f"-> {status_code} "
        f"({elapsed_ms:.2f} ms)\n"
)
    with log_lock:
        with open("server.log", "a") as f:
            f.write(log_entry)

def parse_request(request):
    request_parts = request.split("\r\n\r\n", 1)
    if len(request_parts) == 2:
        request_body = request_parts[1]
    else:
        request_body = ""
    lines = request.splitlines()

    # Parse request line
    request_line = lines[0]
    method, path, version = request_line.split()

    # Parse User-Agent header
    user_agent = ""
    for line in lines:
        if line.startswith("User-Agent: "):
            user_agent = line[len("User-Agent: "):]
    return (method,path,version,user_agent,request_body)

def build_response(status_line, content_type, body):
    return (
        status_line
        + f"Content-Type: {content_type}\r\n".encode()
        + b"Content-Length: "
        + str(len(body)).encode()
        + b"\r\n"
        + b"\r\n"
        + body
    )

def handle_get(path, user_agent):
    content_type="text/plain"
    if path == "/":
        status_line = b"HTTP/1.1 200 OK\r\n"
        body = b"Welcome to Chris's server!"
        status_code=200

    elif path == "/hello":
        status_line = b"HTTP/1.1 200 OK\r\n"
        body = b"Hello!"
        status_code=200

    elif path == "/about":
        status_line = b"HTTP/1.1 200 OK\r\n"
        body = b"Built from scratch using Python sockets."
        status_code=200

    elif path.startswith("/echo/"):
        status_line = b"HTTP/1.1 200 OK\r\n"
        body = path[len("/echo/"):].encode()
        status_code=200

    elif path == "/user-agent":
        status_line = b"HTTP/1.1 200 OK\r\n"
        body = user_agent.encode()
        status_code=200

    elif path == "/api/status":
        uptime_seconds = int(time.time() - server_start_time)

        data = {
            "status": "running",
            "server": "Chris HTTP Server",
            "requests_served": request_count,
            "active_threads": threading.active_count(),
            "uptime_seconds": uptime_seconds
        }
        json_data=json.dumps(data)
        body=json_data.encode()
        content_type="application/json"
        status_line = b"HTTP/1.1 200 OK\r\n"
        status_code=200

    elif path.startswith("/files/"):
        filename = path[len("/files/"):]
        filepath = "files/" + filename
        content_type = (mimetypes.guess_type(filepath)[0] or "application/octet-stream")
        
        try:
            with open(filepath, "r") as f:
                content = f.read()

            status_line = b"HTTP/1.1 200 OK\r\n"
            body = content.encode()
            status_code=200

        except FileNotFoundError:
            status_line = b"HTTP/1.1 404 Not Found\r\n"
            body = b"404 Not Found"
            status_code=404

    else:
        status_line = b"HTTP/1.1 404 Not Found\r\n"
        body = b"404 Not Found"
        status_code=404
    return (status_line,status_code,content_type,body)

def handle_post(path, request_body):
    content_type="text/plain"
    if path.startswith("/files/"):
        filename = path[len("/files/"):]
        filepath = "files/" + filename
        try:
            with open(filepath, "w") as f:
                f.write(request_body)

            status_line = b"HTTP/1.1 201 Created\r\n"
            body = b"File created successfully"
            status_code=201

        except OSError:
            status_line = b"HTTP/1.1 500 Internal Server Error\r\n"
            body = b"Failed to write file"
            status_code=500
    else:
        status_line = b"HTTP/1.1 404 Not Found\r\n"
        body = b"404 Not Found"
        status_code=404
    return (status_line,status_code,content_type,body)

def send_response(client_socket, response):
    client_socket.sendall(response)
    client_socket.shutdown(socket.SHUT_WR)
    client_socket.close()

def handle_client(client_socket,address):

    #Testing if clients work simulataneously by giving more delay

    #import time
    #print(f"START {address}")
    #time.sleep(10)
    #print(f"END {address}")

    start_time = time.perf_counter()
    global request_count
    with request_count_lock:
        request_count += 1

    print(f"Client connected : {address}")

    request = client_socket.recv(1024).decode()
    #print("Raw request:")
    #print(request)
    method, path, version, user_agent, request_body = parse_request(request)
    #print(f"Request Body: {request_body}")
    #print(f"Method: {method}")
    #print(f"Path: {path}")
    #print(f"Version: {version}")
    #print(f"User-Agent: {user_agent}")
    #print("-" * 50)

    # GET ROUTES
        
    if method == "GET":
        status_line, status_code, content_type, body = handle_get(path, user_agent)
        
       
    # POST ROUTES
        
    elif method == "POST":
        status_line, status_code, content_type, body = handle_post(path, request_body)
    # UNSUPPORTED METHODS
    else:
        status_line = b"HTTP/1.1 405 Method Not Allowed\r\n"
        content_type="text/plain"
        body = b"Method Not Allowed"
        status_code=405

    response = build_response(status_line,content_type,body)
    elapsed_ms = (time.perf_counter() - start_time) * 1000

    log_request(method,path,status_code,elapsed_ms)


    send_response(client_socket, response)


def main():
    server_socket = socket.create_server((HOST, PORT))

    print(f"Server listening on {HOST}:{PORT}")
    
    try:
        while True:
            client_socket, address = server_socket.accept()
            thread = threading.Thread(target=handle_client,args=(client_socket, address))
            thread.start()
            print(f"Started thread {thread.ident}")
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        server_socket.close()

    
if __name__ == "__main__":
    main()