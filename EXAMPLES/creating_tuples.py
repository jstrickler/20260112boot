from dataclasses import dataclass

person = "Bill", "Gates", "Microsoft", "1955-10-28"
# person = tuple([....])
print(person, "\n")

print(person[0], person[1], "\n")

first_name, last_name, product, dob = person  # unpack iterable to variables
first_name = person[0]
last_name = person[1]
# ...

print(first_name, last_name, "\n")
print(f"{len(person) = }\n")

# objects with fields
#   tuple
#   named tuple
#   normal hard-coded class
#     class Foo:
#        ....
#   class from dataclasses module
#   pydantic class
#   ????


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int

p1 = Person("John", "Smith", 42)
p2 = Person("Zaphod", "Beeblebrox", 102)
print(f"{p1.first_name = }")
