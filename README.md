# HTTP Server From Scratch

Building an HTTP/1.1 server from scratch using Python sockets.

## Features Completed

- TCP server
- HTTP response generation
- HTTP request parsing
- Basic routing
- 404 handling
- Content-Length header
- Content-Type header

## Current Routes

| Route | Description |
|---------|---------|
| / | Welcome page |
| /hello | Returns greeting |
| /about | About the server |
| anything else | 404 Not Found |

## Example

Request:

```bash
curl http://127.0.0.1:4221/hello