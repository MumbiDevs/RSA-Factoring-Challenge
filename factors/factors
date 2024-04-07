#!/usr/bin/env python

import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: ./run_python_program.py <file>")
        sys.exit(1)

    python_program = "factors.py"  # Name of the Python program
    input_file = sys.argv[1]

    # Execute the Python program with the input file as argument
    subprocess.run(["python", python_program, input_file], check=True)

if __name__ == "__main__":
    main()
