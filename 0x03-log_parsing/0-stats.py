#!/usr/bin/python3
"""Module for task 0"""
import sys
import signal
import re


def print_stats(size, status):
    """Prints the stats"""
    print("File size: {}".format(size))
    for key in sorted(status.keys()):
        if status[key] != 0:
            print("{}: {}".format(key, status[key]))

if __name__ == "__main__":
    status = {"200": 0, "301": 0, "400": 0, "401": 0,
              "403": 0, "404": 0, "405": 0, "500": 0}
    size = 0
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                size += int(data[-1])
            except ValueError:
                pass
            try:
                status[data[-2]] += 1
            except KeyError:
                pass
            if count == 10:
                print_stats(size, status)
                count = 0
        print_stats(size, status)
    except KeyboardInterrupt:
        print_stats(size, status)
        raise


