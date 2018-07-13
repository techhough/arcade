# Example of an instance variable
"""
An instance variable is the type of class variable we’ve used so far.
Each instance of the class gets its own value.
For example, in a room full of people each person will have their own age.
Some of the ages may be the same, but we still need to track each age individually.

With instance variables, we can’t just say “age” with a room full of people.
We need to specify whose age we are talking about.
Also, if there are no people in the room, then referring to an age when there are no people to have an age makes no sense.
"""
class ClassA():
    def __init__(self):
        self.y = 3

# Example of a static variable
"""
With static variables the value is the same for every single instance of the class.
Even if there are no instances, there still is a value for a static variable.
For example, we might have a count static variable for the number of Human classes in existence.
No humans? The value is zero, but the count variable still exists.
"""

class ClassB():
    x = 7

def main():
    # Create class instances
    a = ClassA()
    b = ClassB()

    # Two ways to print the static variable.
    # The second way is the proper way to do it.
    print(b.x)
    print(ClassB.x)

    # One way to print an instance variable.
    # The second generates an error, because we don't know what instance
    # to reference.
    print(a.y)
    #print(ClassA.y)

main()