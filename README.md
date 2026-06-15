# HTTP Server From Scratch

Building an HTTP/1.1 server from scratch using Python sockets.

## Features Completed

* TCP server
* HTTP response generation
* HTTP request parsing
* HTTP header parsing
* Request body parsing
* Basic routing
* Method-based routing (GET and POST)
* Dynamic route handling (`/echo/<text>`)
* User-Agent extraction
* File serving (`/files/<filename>`)
* File creation and updates via POST
* 404 handling
* 201 Created responses
* Content-Length header
* Content-Type header
* File I/O using Python
* Exception handling

## Current Routes

| Route               | Method | Description                  |
| ------------------- | ------ | ---------------------------- |
| `/`                 | GET    | Welcome page                 |
| `/hello`            | GET    | Returns greeting             |
| `/about`            | GET    | About the server             |
| `/echo/<text>`      | GET    | Returns supplied text        |
| `/user-agent`       | GET    | Returns User-Agent header    |
| `/files/<filename>` | GET    | Returns file contents        |
| `/files/<filename>` | POST   | Creates or overwrites a file |
| Any other route     | Any    | 404 Not Found                |

## Example Usage

### Read a File

Request:

```bash
curl http://127.0.0.1:4221/files/test.txt
```

Response:

```text
Hello World
```

### Create or Update a File

Request:

```bash
curl -X POST http://127.0.0.1:4221/files/test.txt -d "Hello World"
```

Response:

```text
File created successfully
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

### Commit 5 - POST File Creation

* Parsed HTTP request bodies
* Added POST support
* Implemented file creation and overwriting
* Added 201 Created responses
* Added write-mode file handling
* Added server-side file persistence

## Technologies Used

* Python
* Socket Programming
* HTTP/1.1
* File I/O
* Git
* GitHub

## Next Steps

* JSON responses
* Static file hosting
* Multithreading
* Logging
* Unit testing
* Persistent connections
* Improved error handling

## Learning Outcomes

Through this project I learned:

* TCP socket programming
* HTTP request/response structure
* HTTP methods (GET and POST)
* HTTP headers
* HTTP status codes
* Request body parsing
* URL routing
* Dynamic route handling
* File serving
* File creation and modification
* Exception handling
* Git and GitHub workflow
* Building backend systems without frameworks

## Future Enhancements

Potential improvements include:

* Serving HTML pages
* JSON API endpoints
* Concurrent client handling
* Request logging
* Configuration files
* Automated testing
* Support for additional HTTP methods
