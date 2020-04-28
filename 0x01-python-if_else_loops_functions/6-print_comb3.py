#!/usr/bin/python3
for n in range(10):
    for i in range(10):
        if n < i:
            print("{:d}{:d}".format(n, i),
                  end="\n" if n is 8 and i is 9 else ", ")
