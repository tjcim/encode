#!/usr/bin/env python3

import sys
import html
import argparse
import urllib.parse


def urlencode(string):
    """URL Encode String."""
    result = []
    for word in string:
        result.append(urllib.parse.quote(word))
    print("".join(result))


def urldecode(string):
    """URL Decode String."""
    result = []
    for word in string:
        result.append(urllib.parse.unquote(word))
    print("".join(result))


def htmlencode(string):
    """HTML Encode String."""
    result = []
    for word in string:
        result.append(html.escape(word))
    print("".join(result))


def htmldecode(string):
    """HTML Decode String."""
    result = []
    for word in string:
        result.append(html.unescape(word))
    print("".join(result))


def decimalencode(string):
    """Encodes ascii characters into decimal, seperates words by new line."""
    if len(string) == 1:
        words = string[0].split()
    else:
        words = string
    for word in words:
        temp = []
        for letter in word:
            temp.append(str(ord(letter)))
        print(" ".join(temp))


def decimaldecode(string):
    result = []
    if type(string) == list and len(string) == 1 and " " in string[0]:
        string = string[0].split()
    for letter in string:
        result.append(chr(int(letter)))
    print("".join(result))


def main(args):
    """Process args."""
    if args.decode:
        if args.url:
            urldecode(args.string)
        if args.html:
            htmldecode(args.string)
        if args.decimal:
            decimaldecode(args.string)
    else:
        if args.url:
            urlencode(args.string)
        if args.html:
            htmlencode(args.string)
        if args.decimal:
            decimalencode(args.string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Encode text into a variety of formats."
    )
    parser.add_argument("-d", "--decode", action="store_true", help="Decode instead of encode.")
    parser.add_argument("-u", "--url", action='store_true', help="URL encode special characters.")
    parser.add_argument("-t", "--html", action='store_true', help="HTML encode special characters.")
    parser.add_argument("--decimal", action="store_true", help="Convert letter to decimal.")
    parser.add_argument("string", nargs="+", default=sys.stdin, help="Text that should be encoded.")
    arglist = sys.argv[1:]
    if not sys.stdin.isatty():
        string = sys.stdin.read()
        arglist.append(string.strip())
    main(parser.parse_args(arglist))
