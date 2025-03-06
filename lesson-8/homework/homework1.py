class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name} the {self.species} says {self.sound}!"
    
    def eat(self, food):
        return f"{self.name} is eating {food}."
    
    def sleep(self):
        return f"{self.name} is sleeping."

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")
    
    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")
    
    def lay_egg(self):
        return f"{self.name} has laid an egg."

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog", "Bark")
    
    def run(self):
        return f"{self.name} is running fast!"

# Creating instances of animals
bessie = Cow("Bessie")
clucky = Chicken("Clucky")
spirit = Dog("Spirit")

# Demonstrating behaviors
print(bessie.make_sound())
print(bessie.eat("grass"))
print(bessie.produce_milk())
print(clucky.make_sound())
print(clucky.lay_egg())
print(spirit.make_sound())
print(spirit.run())