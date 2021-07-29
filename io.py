# Template

import sys
import io
import os


"""
output as a list

arr = [1, 2, 3, 4]
sys.stdout.write(" ".join(map(str, arr)) + "\n")

"""


"""
using list comprehensions
arr = [int(x) for x in stdin.readline().split()]
"""

# taking Input
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# taking Input as a string
number = input().decode()

# Writing to the file
sys.stdout.write(str(number[0]+number[-1])+'\n')


def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    testcases = int(input())
    for test in range(testcases):
        # number = int.from_bytes(input(), "big")
        number = input().decode()
        number = list(map(int, str(number.strip())))
        sys.stdout.write(str(number[0]+number[-1])+'\n')


if __name__ == '__main__':
    main()
