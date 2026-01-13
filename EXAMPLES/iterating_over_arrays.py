fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon']

# for VARIABLE in ITERABLE:
for fruit in fruits:
    if fruit.startswith('ap'):
        continue
    print(fruit)
    # if fruit == 'cherry':
    #     break
print()
print('-' * 60)
for fruit in fruits:
    rfruit = ''.join(sorted(set(fruit)))
    print(rfruit)

def get_lat_lon(zip_code) -> tuple[float, float]:
    # blah blah blah
    return 12.9384, 34.39093

x = get_lat_lon(12345)
print(f"{x[0] = }")


