#pets.py

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def display(self):
        print(f"{self.name} is a {self.species} that is {self.age} years old")
        
