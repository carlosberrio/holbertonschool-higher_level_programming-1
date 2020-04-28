#!/usr/bin/python3
def print_last_digit(number):
    rem = (number if number > 0 else number*(-1)) % 10
    print(rem, end="")
    return rem

#line3 = abs()
