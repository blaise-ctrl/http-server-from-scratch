# HTTP Server From Scratch

Building an HTTP/1.1 server from scratch using Python sockets.

## Features Completed

* TCP server
* HTTP response generation
* HTTP request parsing
* Basic routing
* 404 handling
* Content-Length header
* Content-Type header
* Dynamic route handling (`/echo/<text>`)
* HTTP header parsing
* User-Agent extraction

## Current Routes

| Route           | Description               |
| --------------- | ------------------------- |
| `/`             | Welcome page              |
| `/hello`        | Returns greeting          |
| `/about`        | About the server          |
| `/echo/<text>`  | Returns supplied text     |
| `/user-agent`   | Returns User-Agent header |
| Any other route | 404 Not Found             |

## Example

Request:

```bash
curl http://127.0.0.1:4221/hello
```

Response:

```text
Hello!
```

## Project Structure

```text
http-server-from-scratch/
│
├── server.py
├── README.md
└── .gitignore
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

## Technologies Used

* Python
* Socket Programming
* HTTP/1.1
* Git
* GitHub

## Next Steps

* File serving (`/files/<filename>`)
* POST request handling
* JSON responses
* Multithreading
* Logging
* Unit testing

## Learning Outcomes

Through this project I learned:

* TCP socket programming
* HTTP request/response structure
* HTTP headers
* URL routing
* Dynamic route handling
* Git and GitHub workflow
* Building backend systems without frameworks
