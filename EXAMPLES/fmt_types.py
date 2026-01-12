person = 'Bob'
value = 488
result = .5617282027


print(f'{person:s}')   # String 
print(f'{value:d}')    # Integer (displayed as decimal)
print(f'{value:b}')    # Integer (displayed as binary)
print(f'{value:o}')    # Integer (displayed as octal)
print(f'{value:x}')    # Integer (displayed as hex)
print(f'{value:X}')    # Integer (displayed as hex with uppercase digits)
print(f'{result:f}')    # Float (defaults to 6 places after the decimal point)
print(f'{result:.2f}')    # Float rounded to 2 decimal places
print(f'{result:.2%}')    # Float converted to percent and rounded to 2 decimal places
