#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(argc, "" if argc is 1 else "s", "." if argc is 0 else ":"))
    for idx in range(argc):
        print("{}: {}".format(idx + 1, sys.argv[idx + 1]))
