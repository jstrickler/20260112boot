from datetime import date

today = date.today()

print(f"type(today): {type(today)}")
print("tomorrow =", today)   # uses str(today)
print()
print("torquay = ",repr(today))  # uses repr(today)
print()
print(f"{today = }")  # also uses repr(today)
print(f"{today = !s}")  # also uses repr(today)
