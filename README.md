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
- Dynamic route handling (/echo/<text>)
- HTTP header parsing
- User-Agent extraction

## Current Routes

| Route | Description |
|---------|---------|
| / | Welcome page |
| /hello | Returns greeting |
| /about | About the server |
| /echo/<text> | Returns supplied text |
| /user-agent | Returns User-Agent header |
| anything else | 404 Not Found |

## Example

Request:

```bash
curl http://127.0.0.1:4221/hello

## Development Log

### Commit 1
- Created TCP server
- Added HTTP response generation

### Commit 2
- Added request parsing
- Added routing
- Added 404 handling

### Commit 3
- Added dynamic echo endpoint
- Added User-Agent header parsing


## Next Steps

- File serving
- POST requests
- JSON responses
- Multithreading