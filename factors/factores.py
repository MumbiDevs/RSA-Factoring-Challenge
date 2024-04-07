#!/usr/bin/env python

import sys

def factorize_number(number):
    flag = True
    divisor = 2
    while flag:
        remainder = number % divisor
        if remainder == 0:
            counter = number // divisor
            print(f"{number}={counter}*{divisor}")
            flag = False
        divisor += 1

def main():
    if len(sys.argv) != 2:
        print("Usage: ./factores.py <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            factorize_number(number)

if __name__ == "__main__":
    main()
