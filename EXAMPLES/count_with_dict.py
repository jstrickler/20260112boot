counts = {}  # create new empty dict

with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        breakfast_item = line.rstrip()
        if breakfast_item in counts:   # check to see if current item in dict
            counts[breakfast_item] = counts[breakfast_item] + 1   # if so, increment count for specified key
        else:
            counts[breakfast_item] = 1 # else add new element 

def by_value(item):
    return item[1], item[0]

for item, count in sorted(counts.items(), key=by_value):
    print(item, count)
