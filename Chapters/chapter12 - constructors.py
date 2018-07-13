class Dog():
    name = ""

    def __init__(self, my_name): #constructor. Method that automatically runs as a class is created. Initialise and set up data in class.
        print("A new dog has been born!")
        self.name = my_name

myDog = Dog("Jules")
print("The dog's name is: ", myDog.name)

herDog = Dog("Spot")
print("The dog's name is: ", herDog.name)