#!/usr/bin/env python3

import sys
import html
import argparse
import urllib.parse


def urlencode(string):
    """URL Encode String."""
    return urllib.parse.quote(string)


def urldecode(string):
    """URL Decode String."""
    return urllib.parse.unquote(string)


def htmlencode(string):
    """HTML Encode String."""
    return html.escape(string)


def htmldecode(string):
    """HTML Decode String."""
    return html.unescape(string)


def main(args):
    """Process args."""
    if args.decode:
        if args.url:
            print(urldecode(args.string))
        if args.html:
            print(htmldecode(args.string))
    else:
        if args.url:
            print(urlencode(args.string))
        if args.html:
            print(htmlencode(args.string))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Encode text into a variety of formats."
    )
    parser.add_argument("-d", "--decode", action="store_true", help="Decode instead of encode.")
    parser.add_argument("-u", "--url", action='store_true', help="URL encode special characters.")
    parser.add_argument("-t", "--html", action='store_true', help="HTML encode special characters.")
    parser.add_argument("string", nargs="?", default=sys.stdin, help="Text that should be encoded.")
    arglist = sys.argv[1:]
    if not sys.stdin.isatty():
        string = sys.stdin.read()
        arglist.append(string.strip())
    main(parser.parse_args(arglist))
