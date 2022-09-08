# __main__.py

import sys
from rpchecker.cli import read_user_cli_args

def main():
    """"run RP Checker"""
    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)
    if not urls:
        print("Error: no URLs to check", file=sys.stderr)
        sys.exit()
        _synchronous_check(urls)