# cli.py

import argparse

def read_user_cli_args():
    """ """
    parser = argparse.ArgumentParser(
        prog="rpchecker",
        description="check the availabiluty of websites"
    )

    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter on or more website URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )
    return parser.parse_args()

def display_check_results(result, url, error=""):
    """"Displays the result of the a connectivity check"""
    print(f'The status of the "{url}" is :', end=" ")
    if result:
        print('"Online!"')
    else:
        print(f'"Offline" \n Error: "{error}')