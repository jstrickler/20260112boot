import os
from pprint import pprint

DIRECTORY = '../DATA'

for entry in os.scandir(DIRECTORY):
    stat_info = entry.stat()
    print(f"{entry.name:25s} {stat_info.st_size:10d} {entry.is_file()!s:5s} {entry.is_dir()!s:5s} {stat_info.st_mode:06o}")
print('-' * 60)

names = dict([(e.name,e.stat().st_size) for e in os.scandir(DIRECTORY)])
pprint(names)
