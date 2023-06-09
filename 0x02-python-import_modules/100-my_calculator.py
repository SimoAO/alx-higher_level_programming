#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] in list(op.keys()):
        print("{} {} {} = {}"
                .format(argv[1], argv[2], argv[3], op[argv[2]](int(argv[1]), int(argv[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
