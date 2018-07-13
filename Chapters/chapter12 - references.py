class Person:
    name = ""
    money = 0

bob = Person() #bob is not the object, just a pointer to the object!
bob.name = "Bob"
bob.money = 100

nancy = bob #nancy is now pointing at the same object bob points to. This does not create 2 objects.
nancy.name = "Nancy"

print(bob.name,"has",bob.money,"dollars.")
print(nancy.name,"has",nancy.money,"dollars.")