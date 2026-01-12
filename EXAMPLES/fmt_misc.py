'''Demonstrate misc formatting'''

big_number = 2303902390239

print(f"Big number: {big_number:,d}")  # Add commas for readability
print()

value = 27

print(f"Binary: {value:#010b}")  # Binary format with leading 0b
print(f"Octal:  {value:#010o}")  # Octal format with leading 0o
print(f"Hex:    {value:#010x}")  # Hexadecimal format with leading 0x
print()
