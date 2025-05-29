import argparse
from caching_proxy.caching_proxy import start_proxy, clear_cache


def main() -> None:

    parser = argparse.ArgumentParser(prog="caching-proxy",
                                     description='Caching Proxy CLI Tool')

    subparsers = parser.add_subparsers(dest="command",
                                       help="Available commands")

    start_parser = subparsers.add_parser("start",
                                         help="Start Caching Proxy")
    start_parser.add_argument("-p", "--port", type=int, default=8080, help="Port number to run the proxy")
    start_parser.add_argument("-o", "--origin", type=str, help="URL to cache")

    clear_parser = subparsers.add_parser("clear-cache",
                          help="Clear all cached data")
    clear_parser.add_argument("-p", "--port", type=int, help="Port number to clear cached data")


    args = parser.parse_args()

    commands = {
        "start": lambda: start_proxy(args.origin, args.port),
        "clear-cache": lambda: clear_cache(args.port),
    }

    if args.command in commands:
        commands[args.command]()
    else:
        parser.print_help()


