#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    return 98 + a ** b

# Call the function with some values
result = magic_calculation(2, 3)

# Disassemble the function to see its bytecode
dis.dis(magic_calculation)

