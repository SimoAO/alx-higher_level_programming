#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = {"+": add, "-": sub, "/": div}
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] in list(op.keys()):
        print("{} {} {} = {}"
                .format(a, argv[2], b, op[argv[2]](a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
