
## Caching Proxy Server
Cache Proxy is a simple, bare-bones caching proxy server implemented in Python. It serves as a basic solution for caching HTTP requests and responses, using an in-memory map to store the cache.

## Features
- In-Memory Caching:
  - The server uses an in-memory map to store cached responses. This approach allows for fast lookups and reduces the time needed to retrieve cached data.

- Proxy Functionality:
  - The server forwards client requests to the target server and caches the responses. If the same request is made again, the server returns the cached response, saving the time and resources of making a new request to the target server.

- Simple Design:
  - This is a minimalistic implementation aimed at demonstrating the core concepts of a caching proxy server. It is not suitable for production use without further enhancements.

## Usage

### Start the server:

```bash
caching-proxy start --port 8083 --origin www.google.com
```

### To clear the cache::

```bash
caching-proxy clear-cache --port
```

