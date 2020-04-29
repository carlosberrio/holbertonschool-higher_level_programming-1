# 0x01. Python - if/else, loops, functions

0. Program that assigns a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

1. The last digit. xProgram that assigns a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

2. Program that prints the ASCII alphabet, in lowercase, not followed by a new line.
'c' => Converts the integer to the corresponding unicode character before printing.

3. Program that prints the ASCII alphabet, in lowercase, not followed by a new line.

4. Program that prints all numbers from 0 to 98 in decimal and in hexadecimal.
'x' => Outputs the number in base 16, using lower- case letters for the digits above 9.

7. islower. Function that checks for lowercase character.

8. To uppercase. Function that prints a string in uppercase followed by a new line.

9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important. Function that prints the last digit of a number.

10. a + B. Function that adds two integers and returns the result.

11. a ^ b. Function that computes a to the power of b and return the value.

12. Fizz Buzz. Function that prints the numbers from 1 to 100 separated by a space.
For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

13. Insert in sorted linked list. Function in C that inserts a number into a sorted singly linked list.

* with dis module:
```bash
#!/usr/bin/python3
import dis
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    return a * b - c

dis.dis(magic_calculation)
```
### Author:
* Tatiana Orejuela Zapata | [Github](https://github.com/tatsOre)

##### Foundations - Higher-level programming  Python
##### April, 2020. Cali, Colombia.