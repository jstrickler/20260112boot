city = 'Orlando' 
temperature = 85
hit_count = 5
average = 3.4563892382

print(city, temperature, hit_count, average)
print()

print(city, end=' ')  # Print space instead of newline at the end
print(temperature)
print()

# Item separator is comma + space
print(city, temperature, hit_count, average, sep=", ")
print()

# Item separator is empty string
print(city, temperature, hit_count, average, sep="\n")
print()
# default behavior
print(city, temperature, hit_count, average, sep=" ", end="\n")
print()
print(city + ", " +  str(temperature))
print(f"{city}, {10 * temperature}")  # f-string AKA format string

print(f"Average is {average}")
print("Average is {}".format(average))  # .format() METHOD
print(f"Average is {average:.2f}")
pct = .234323
print(f"Average is {pct:.2%}")
