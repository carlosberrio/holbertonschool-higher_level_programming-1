# 0x00. Python - Hello, World

0. Run Python file: Shell script that runs a Python script.
The Python file name will be saved in the environment variable $PYFILE

1. Run inline: Shell script that runs Python code.
The Python code will be saved in the environment variable $PYCODE

2. Hello, print mandatory: write a Python script that prints exactly ' \"Programming is like building a multilingual puzzle ', followed by a new line, using the function print.

3. Print integer: complete a source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
Result: 98 Battery street.

4. Print float: complete a source code in order to print the float stored in the variable number with a precision of 2 digits.

5. Print string: complete 3 times the value of str, followed by a new line, followed by the 9 first characters of str, followed by a new line.
Loops or conditional statement are not allowed and the program should be maximum 5 lines long

6. Play with strings: concat to sentences to print "Welcome to Holberton School!"

7. Copy - Cut - Paste word = "Holberton":
- word_first_3 should contain the first 3 letters of the variable word
- word_last_2 should contain the last 2 letters of the variable word
- middle_word should contain the value of the variable word without the first and last letters

8. Create a new sentence slicing another sentence.

9. Easter Egg: write a Python script that prints The Zen of Python, by TimPeters, followed by a new line.

10. Linked list cycle: function in C that checks if a singly linked list has a cycle in it.

11. Hello, write: Python script that prints exactly: and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line. Function write from the sys module / print is not allowed / script should print to stderr / exit with status 1

12. Compile: script that compiles a Python script file.
The Python file name will be stored in the environment variable $PYFILE
The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

#### '.pyc' files in Python:
Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler. This means that source files can be run directly without explicitly creating an executable which is then run. '.pyc' files contain byte code, which is what the Python interpreter compiles the source to. This code is then executed by Python's virtual machine.

13. ByteCode -> Python #1
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

#### Disassembly of def magic_calculation(a, b):

3             0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE

* Bytecode instructions:
"3" is the line number
LOAD_CONST = Pushes co_consts[consti] onto the stack
LOAD_FAST = Pushes a reference to the local co_varnames[var_num] onto the stack
BINARY_POWER = POW OPR (TOS1 ** TOS)
BINARY_ADD = SUM (TOS1 + TOS)
RETURN_VALUE Return with TOS to the caller of the function

* TOS = top-of-stack
* Binary operations remove the top of the stack (TOS) and the second top-most stack item (TOS1) from the stack. They perform the operation, and put the result back on the stack.
* Second numeric column =  offsets

* Python complete script to check instructions:
#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    return 98 + a ** b

dis.dis(magic_calculation)

### Author:
* Tatiana Orejuela Zapata | [Github](https://github.com/tatsOre)

##### Foundations - Higher-level programming  Python
##### April, 2020. Cali, Colombia.