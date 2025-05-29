import requests
from cachetools import TTLCache
from flask import Flask, request, Response


cache = TTLCache(maxsize=50, ttl=300)

def start_proxy(origin: str, port: int) -> None:

    if not origin.startswith(("http://","https://") ):
        schema_origin = f"http://{origin}"
    else:
        schema_origin = origin

    app = Flask(__name__)

    @app.route("/", defaults={"path": ""}, methods=["GET"])
    @app.route("/<path:path>", methods=["GET"])
    def proxy(path: str) -> Response:

        cache_key = request.full_path

        if cache_key in cache:
            cache_value = cache[cache_key]
            response = Response(cache_value.data, cache_value.status, cache_value.headers)
            response.headers["X-Cache"] = "HIT"
        else:
            url = f"{schema_origin}/{path}"
            upstream = requests.get(url, params=request.args)
            response =  Response(upstream.content, upstream.status_code, upstream.headers)
            cache[cache_key] = response
            response.headers["X-Cache"] = "MISS"

        print(response.headers['X-Cache'])

        return response

    @app.route('/_cache/clear', methods=['POST'])
    def clear_cache_endpoint():
        cache.clear()
        return {"status": "success", "cleared_entries": len(cache)}, 200

    app.run(port=port)

def clear_cache(port: int) -> Response:
    url = f"http://127.0.0.1:{port}/_cache/clear"
    try:
        response = requests.post(url)
        return response
    except requests.exceptions.ConnectionError:
        raise ConnectionError(f"Could not connect to proxy server on port {port}. Is it running?")



