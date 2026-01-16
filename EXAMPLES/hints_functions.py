def shout(word: str, times: int = 1) -> str:
    return word.upper() * times

a: str = shout('Python', 3)
print(f"{a = }")
b: int = shout('Python', 3)
print(f"{b = }")
print()
c: str = shout(b'foo', 10)
print(f"{c = }")


def read_files(*file_paths: str) -> None:
    for file_path in file_paths:
        print(f"Opening {file_path}")
        with open(file_path) as file_in:
            pass

read_files('../DATA/mary.txt', '../DATA/parrot.txt')
print()

def shout_various(**kwargs: int) -> None: # argument values must be ints
    for word, count in kwargs.items(): # loop through named arguments
        print(word.upper() * count)

shout_various(python=10, perl=1, c=3, cobol=3)

a: list[int]
b: list[float]
c: list[int|float]
Number = int | float  # compound type
d: list[Number]

e: tuple[int, int, float]
e = 5, 10, 18.9
e = 5.2, 5, 5
e = 1, 2, 3, 4

f: tuple[str, ...]
f = "foo",
f = "foo", "bar", "blah"
f = ()

g: dict[str, int]
h: dict[str, list[float]]
i: set[str]

StringLike = str | bytes

ArgType = str | None












