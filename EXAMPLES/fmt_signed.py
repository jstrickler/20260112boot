values = 123, -321, 14, -2, 0

for value in values:
    print(f"default: |{value:4d}|")  # default (pipe symbols just to show white space)
print()

for value in values:
    print(f"   plus: |{value:+4d}|")  # plus sign puts '+' on positive numbers (and zero) and '-' on negative
print()

for value in values:
    print(f"  minus: |{value:-4d}|") # minus sign only puts '-' on negative numbers
print()

for value in values:
    print(f"  space: |{value: d}|") # space puts '-' on negative numbers and space on others
print()
