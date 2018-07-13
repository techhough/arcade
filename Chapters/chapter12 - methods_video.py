"""
Video content
http://arcade-book.readthedocs.io/en/latest/chapters/12_classes/classes.html
"""

class Dog():
    age=0
    name=""
    weight=0

    def bark(self): #This self allows us to refer back to the class and say "my age, my name, and my weight"
        print(self.name,"says 'Woof'")

    def poop(self):
        self.weight -= 0.25

my_dog = Dog()
my_dog.name = "Jules"
my_dog.weight = 35

my_dog2 = Dog()
my_dog2.name = "Jack"
my_dog2.weight = 28

my_dog.bark()
my_dog2.bark()

print(my_dog.weight)
print(my_dog2.weight)

my_dog.poop()

print(my_dog.weight)
print(my_dog2.weight)