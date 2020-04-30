#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for idx in range(len(sys.argv) - 1):
        sum += int(sys.argv[idx + 1])
    print(sum)
