spam = {
    'a': 10,
    'b': 20,
    'c': 30,
}

ham = {
    'c': 100, # will overwrite previous value
    'd': 200,
    'e': 300,
}

spam.update(ham)
print(f"{spam = }")
