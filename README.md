# HTTP Server From Scratch

Building an HTTP/1.1 server from scratch using Python sockets.

## Features Completed

* TCP server
* HTTP response generation
* HTTP request parsing
* HTTP header parsing
* Basic routing
* Method-based routing (GET)
* Dynamic route handling (`/echo/<text>`)
* User-Agent extraction
* File serving (`/files/<filename>`)
* 404 handling
* Content-Length header
* Content-Type header
* File I/O using Python

## Current Routes

| Route               | Description                |
| ------------------- | -------------------------- |
| `/`                 | Welcome page               |
| `/hello`            | Returns greeting           |
| `/about`            | About the server           |
| `/echo/<text>`      | Returns supplied text      |
| `/user-agent`       | Returns User-Agent header  |
| `/files/<filename>` | Returns contents of a file |
| Any other route     | 404 Not Found              |

## Example

Request:

```bash
curl http://127.0.0.1:4221/files/test.txt
```

Response:

```text
Hello from a file!
```

## Project Structure

```text
http-server-from-scratch/
│
├── server.py
├── README.md
├── .gitignore
└── files/
    └── test.txt
```

## Development Log

### Commit 1 - Initial HTTP Server

* Created TCP socket server
* Accepted client connections
* Sent HTTP responses

### Commit 2 - Request Parsing and Routing

* Parsed HTTP request line
* Extracted method, path and version
* Added `/hello` and `/about` routes
* Added 404 handling
* Added Content-Length and Content-Type headers

### Commit 3 - Dynamic Routes and Header Parsing

* Added `/echo/<text>` endpoint
* Parsed HTTP headers
* Extracted User-Agent header
* Added `/user-agent` endpoint

### Commit 4 - File Serving

* Added `/files/<filename>` endpoint
* Implemented file reading using Python file I/O
* Added FileNotFoundError handling
* Returned file contents as HTTP response body
* Refactored routing by HTTP method

## Technologies Used

* Python
* Socket Programming
* HTTP/1.1
* File I/O
* Git
* GitHub

## Next Steps

* POST request handling
* File creation via POST
* JSON responses
* Multithreading
* Logging
* Unit testing

## Learning Outcomes

Through this project I learned:

* TCP socket programming
* HTTP request/response structure
* HTTP headers
* HTTP status codes
* URL routing
* Dynamic route handling
* File serving
* Exception handling
* Git and GitHub workflow
* Building backend systems without frameworks
