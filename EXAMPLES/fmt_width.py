name = 'Ann Elk'
value = 10000
airspeed = 22.347
# note: [] are used to show blank space, and are not part of the formatting
print(f'[{name:s}]')     # Default format -- no padding
print(f'[{name:10s}]')   # Left justify, 10 characters wide
print(f'[{name:3s}]')    # Left justify, 3 characters wide, displays entire string
print(f'[{name:3.3s}]')  # Left justify, 3 characters wide, truncates string to max width
print()
print(f'[{value:8d}]')       # Right justify, decimal, 8 characters wide (all numbers are right-justified by default)
print(f'[{value:8f}]')       # Right justify int as float, 8 characters wide
print(f'[{airspeed:8f}]')    # Right justify float as float, 8 characters wide
print(f'[{airspeed:.2f}]')   # Right justify, float, 3 decimal places, no maximum width
print(f'[{airspeed:8.3f}]')  # Right justify, float, 3 decimal places, maximum width 8
