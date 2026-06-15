import socket

HOST = "127.0.0.1"
PORT = 4221


def main():
    server_socket = socket.create_server((HOST, PORT))

    print(f"Server listening on {HOST}:{PORT}")
    

    while True:
        client_socket, address = server_socket.accept()

        print(f"Client connected: {address}")

        request = client_socket.recv(1024).decode()
        print("Raw request:")
        print(request)

        request_parts = request.split("\r\n\r\n", 1)
        if len(request_parts) == 2:
            request_body = request_parts[1]
        else:
            request_body = ""
        
        print(f"Request Body: {request_body}")

        lines = request.splitlines()

        # Parse request line
        request_line = lines[0]
        method, path, version = request_line.split()

        # Parse User-Agent header
        user_agent = ""
        for line in lines:
            if line.startswith("User-Agent: "):
                user_agent = line[len("User-Agent: "):]

        print(f"Method: {method}")
        print(f"Path: {path}")
        print(f"Version: {version}")
        print(f"User-Agent: {user_agent}")
        print("-" * 50)

        
        # GET ROUTES
        
        if method == "GET":

            if path == "/":
                status_line = b"HTTP/1.1 200 OK\r\n"
                body = b"Welcome to Chris's server!"

            elif path == "/hello":
                status_line = b"HTTP/1.1 200 OK\r\n"
                body = b"Hello!"

            elif path == "/about":
                status_line = b"HTTP/1.1 200 OK\r\n"
                body = b"Built from scratch using Python sockets."

            elif path.startswith("/echo/"):
                status_line = b"HTTP/1.1 200 OK\r\n"
                body = path[len("/echo/"):].encode()

            elif path == "/user-agent":
                status_line = b"HTTP/1.1 200 OK\r\n"
                body = user_agent.encode()

            elif path.startswith("/files/"):
                filename = path[len("/files/"):]
                filepath = "files/" + filename

                try:
                    with open(filepath, "r") as f:
                        content = f.read()

                    status_line = b"HTTP/1.1 200 OK\r\n"
                    body = content.encode()

                except FileNotFoundError:
                    status_line = b"HTTP/1.1 404 Not Found\r\n"
                    body = b"404 Not Found"

            else:
                status_line = b"HTTP/1.1 404 Not Found\r\n"
                body = b"404 Not Found"

       
        # POST ROUTES
        
        elif method == "POST":
            if path.startswith("/files/"):
                filename = path[len("/files/"):]
                filepath = "files/" + filename
                try:
                    with open(filepath, "w") as f:
                        f.write(request_body)

                    status_line = b"HTTP/1.1 201 Created\r\n"
                    body = b"File created successfully"

                except OSError:
                    status_line = b"HTTP/1.1 500 Internal Server Error\r\n"
                    body = b"Failed to write file"
            else:
                status_line = b"HTTP/1.1 404 Not Found\r\n"
                body = b"404 Not Found"
        # UNSUPPORTED METHODS

        else:
            status_line = b"HTTP/1.1 405 Method Not Allowed\r\n"
            body = b"Method Not Allowed"

        response = (
            status_line
            + b"Content-Type: text/plain\r\n"
            + b"Content-Length: "
            + str(len(body)).encode()
            + b"\r\n"
            + b"\r\n"
            + body
        )

        client_socket.sendall(response)

        client_socket.shutdown(socket.SHUT_WR)
        client_socket.close()


if __name__ == "__main__":
    main()