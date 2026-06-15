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
        request_line=request.splitlines()[0]
        method,path,version=request_line.split()
        print(f"Method:{method}")
        print(f"Path:{path}")
        print(f"Version:{version}")
        print("-" * 50)

        if path == "/":
            status_line = b"HTTP/1.1 200 OK\r\n"
            body = b"Welcome to Chris's server!"
        elif path == "/hello":
            status_line = b"HTTP/1.1 200 OK\r\n"
            body = b"Hello!"

        elif path == "/about":
            status_line = b"HTTP/1.1 200 OK\r\n"
            body = b"Built from scratch using Python sockets."

        else:
            status_line = b"HTTP/1.1 404 Not Found\r\n"
            body = b"404 Not Found"

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