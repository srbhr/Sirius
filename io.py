# Template

import sys
import io
import os


# output as a list
#     arr = [1, 2, 3, 4]
#   sys.stdout.write(" ".join(map(str, arr)) + "\n")

# arr = [int(x) for x in stdin.readline().split()]

def program():
    return None


def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    testcases = int(input())
    for test in range(testcases):
        number = int(input())
        sys.stdout.write(str(program)+'\n')


if __name__ == '__main__':
    main()
