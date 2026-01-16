import re
import fileinput
import argparse

# from X import y
# import X; X.y

def main():
    args = get_args()  # args.i args.f args.pattern args.file_list
    do_search(args)

def do_search(args):
    rx_search_term = re.compile(args.pattern, re.IGNORECASE if args.ignore_case else 0)
    for raw_line in fileinput.input(args.file_list):
        if rx_search_term.search(raw_line):
            if args.show_names:
                print(fileinput.filename(), end=" ")
            print(raw_line.rstrip())

def get_args():
    parser = argparse.ArgumentParser(
        description="""
            Faux Grep

            Python implementation of Unix grep command
            """
    )
    parser.add_argument('-i', '--ignore_case', dest="ignore_case", action="store_true", help="ignore case")
    parser.add_argument('-f', dest="show_names", action="store_true", help="show file name")

    parser.add_argument('pattern', help="pattern to find")

    parser.add_argument('file_list', nargs="*", help="file names")

    return parser.parse_args()



if __name__ == "__main__":
    main()