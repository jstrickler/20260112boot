def hello():
    print("Hello")

x = hello()
print(f"{x = }")

hello()
print("Not hello")
hello()

def square_root(x):
    return x ** .5

print(square_root(2))

def grep1(search_term, file_path):
    with open(file_path) as file_in:
        for raw_line in file_in:
            if search_term in raw_line:
                print(raw_line.rstrip())

grep1('chicken', 'DATA/parrot.txt')
print('-' * 60)

# \b[a-z]{8,}}\b

def grep2(search_term: str, *file_path_list: ):
    for file_path in file_path_list: # file_path_list is a tuple of args
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    print(raw_line.rstrip())

grep2('chicken', 'DATA/parrot.txt', 'DATA/words.txt', 'DATA/alice.txt')
print('-' * 60)

grep2('lizard', 'DATA/parrot.txt', 'DATA/words.txt', 'DATA/alice.txt')
print('-' * 60)

def grep3(search_term: str, *file_path_list: str, ignore_case: bool=False) -> None:
    """
    grep3 search one or more files for a search term

    Usage:
    grep3(search_term: str, *files: str, ignore_case: bool)
    """
    for file_path in file_path_list: # file_path_list is a tuple of args
        if ignore_case:
            search_term = search_term.lower()
        with open(file_path) as file_in:
            for raw_line in file_in:
                search_line = raw_line.lower() if ignore_case else raw_line
                if search_term in search_line:
                    print(raw_line.rstrip())

grep3('lizard', 'DATA/parrot.txt', 'DATA/words.txt', 'DATA/alice.txt', ignore_case=True)
print('-' * 60)

grep3('lizard', 'DATA/parrot.txt', 'DATA/words.txt', 'DATA/alice.txt')
print('-' * 60)

import typing  # as T

def grep4(search_term: str, file_paths: typing.Iterable):
    pass

grep4('wombat', ['file1', 'file2' 'file3'])

def foom(items: typing.Collection):
    pass
