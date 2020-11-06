#!/usr/bin/env python3
"""
Rates
"""

import os


__author__ = "Brian McMichael"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    increment = 0.25
    for i in range(401):
        rate = i * increment
        stream = os.popen(f'./mcd-cli/bin/mcd duty {rate}')
        output = stream.read().rstrip()
        rate = '%.2f' % rate
        #print(f"rates[{int(rate * 100)}] = {output};")
        print(f"{rate:>6}%: {output}")
        #print(f"{output},")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
