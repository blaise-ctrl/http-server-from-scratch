# HTTP Server From Scratch

Building a multithreaded HTTP/1.1 server from scratch using Python sockets without any web frameworks.

## Features Completed

* TCP socket server
* HTTP/1.1 request parsing
* HTTP response generation
* HTTP header parsing
* HTTP request body parsing
* GET request handling
* POST request handling
* Dynamic URL routing
* User-Agent extraction
* File serving
* File creation and overwriting
* JSON API responses
* Multithreaded client handling
* Thread-safe request counting
* Thread-safe logging
* Dynamic Content-Type handling
* Content-Length header generation
* HTTP status code handling
* Exception handling
* Git version control

## Current Routes

| Route               | Method | Description                       |
| ------------------- | ------ | --------------------------------- |
| `/`                 | GET    | Welcome page                      |
| `/hello`            | GET    | Returns greeting                  |
| `/about`            | GET    | Returns server information        |
| `/echo/<text>`      | GET    | Echoes supplied text              |
| `/user-agent`       | GET    | Returns User-Agent header         |
| `/files/<filename>` | GET    | Returns contents of a file        |
| `/files/<filename>` | POST   | Creates or overwrites a file      |
| `/api/status`       | GET    | Returns server statistics in JSON |
| Any other route     | Any    | Returns 404 Not Found             |

## Example Requests

### Basic Route

```bash
curl http://127.0.0.1:4221/hello
```

Response:

```text
Hello!
```

### File Read

```bash
curl http://127.0.0.1:4221/files/test.txt
```

Response:

```text
Hello World
```

### File Write

```bash
curl -X POST http://127.0.0.1:4221/files/test.txt -d "Hello World"
```

Response:

```text
File created successfully
```

### JSON API

```bash
curl http://127.0.0.1:4221/api/status
```

Response:

```json
{
    "status": "running",
    "server": "Chris HTTP Server",
    "requests_served": 42
}
```

## Project Structure

```text
http-server-from-scratch/
│
├── server.py
├── README.md
├── .gitignore
├── server.log
└── files/
    ├── test.txt
    ├── test.html
    └── test.json
```

## Development Log

### Commit 1 - Initial HTTP Server

* Created TCP socket server
* Accepted client connections
* Generated HTTP responses

### Commit 2 - Request Parsing and Routing

* Parsed HTTP request line
* Extracted method, path and version
* Added route handling
* Added 404 responses
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
* Refactored routing by HTTP method

### Commit 5 - File Creation via POST

* Parsed HTTP request bodies
* Added POST support
* Implemented file creation and overwriting
* Added HTTP 201 Created responses
* Added file persistence

### Commit 6 - Concurrency and Logging

* Added multithreaded client handling
* Implemented thread-safe logging
* Added request logging with timestamps
* Added thread-safe request counters

### Commit 7 - JSON API and Content Handling

* Added JSON status endpoint
* Implemented request statistics API
* Added dynamic Content-Type handling
* Improved response generation
* Refactored server architecture

## Technologies Used

* Python
* Socket Programming
* Multithreading
* HTTP/1.1
* JSON
* File I/O
* Git
* GitHub

## Key Concepts Demonstrated

* TCP/IP Networking
* Socket Programming
* HTTP Protocol Internals
* Request Parsing
* Response Construction
* Concurrent Programming
* Thread Synchronization
* Race Condition Prevention
* File Systems
* REST-style APIs
* JSON Serialization
* Logging Systems
* Software Architecture

## Learning Outcomes

Through this project I learned:

* How HTTP works under the hood
* How browsers and clients communicate with servers
* How to parse raw HTTP requests
* How to generate HTTP responses manually
* How multithreaded servers handle concurrent clients
* How race conditions occur and how locks prevent them
* How REST APIs return structured JSON data
* How backend systems persist data using files
* How logging systems track server activity
* How to organize and refactor growing codebases
* How to use Git and GitHub effectively

## Future Enhancements

* Persistent connections (Keep-Alive)
* Static website hosting
* Request compression
* Configuration files
* Unit testing
* Docker support
* HTTPS/TLS support
* Additional HTTP methods (PUT, DELETE)

## Sample Log Output

```text
2026-06-17 14:22:01 GET /hello -> 200
2026-06-17 14:22:05 GET /about -> 200
2026-06-17 14:22:10 POST /files/test.txt -> 201
2026-06-17 14:22:15 GET /api/status -> 200
```
