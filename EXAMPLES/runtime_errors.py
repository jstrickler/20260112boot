PATH = "../DATA/mary.txt"

file_in = None
try:
    print(5 / 0)
    file_in = open(PATH)
except (PermissionError, FileNotFoundError) as err:
    print(f"Sorry, {PATH} not found")
except Exception as err:
    print(f"Wow, did not expect {err}")
else:
    contents = file_in.read()
    print(contents)
finally:
    if file_in:
        file_in.close()

print("more stuff going on...")