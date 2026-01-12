spam = {
    'a': 10,
    'b': 20,
    'c': 30,
}

ham = {
    'c': 100, # will NOT overwrite previous value
    'd': 200,
    'e': 300,
}

for letter, value in ham.items():
    spam.setdefault(letter, value)
print(f"{spam = }")
