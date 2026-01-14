states = []   # states = list()
states.append('Ohio')
states.append("Michigan")

name = "Fred"  # name = str("Fred")

class Dog:  #  UpperCamelCase   DBConnection  FileRepository  WombatGizmo
    def  __init__(self, name):
        self._name = name
        
    def bark(self):  # method
        print("woof woof")

d1 = Dog('Rosie')  # d1 is INSTANCE of Dog class
d2 = Dog('Andy')
d3 = Dog('Nellie')
d1.bark()


