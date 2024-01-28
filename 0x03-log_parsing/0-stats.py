#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys
import re


def print_stats(status_codes, file_size):
    """ print stats """
    print("File size: {}".format(file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    counter = 0
    try:
        for line in sys.stdin:
            counter += 1
            try:
                file_size += int(re.split(" ", line)[-1])
            except ValueError:
                pass
            try:
                status_codes[re.split(" ", line)[-2]] += 1
            except KeyError:
                pass
            if counter == 10:
                print_stats(status_codes, file_size)
                counter = 0
        print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
