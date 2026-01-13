states = [
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
]
# w -> destroy contents
# a -> append to contents
# x -> open only if file does not exist
with open("states.txt", "w") as states_out: # "w" opens for writing, "a" for append
    for state in states:
        states_out.write(state + "\n")  # write() does not automatically add newline

# FILE.writelines(ITERABLE)