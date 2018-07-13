class Car(object):
    #class attribute that applies to every instance this class could ever make
    wheels = 4

    def __init__(self, make, model):
        #instance variables that have values which change from instance to instance
        self.make = make
        self.model = model

mustang = Car('Ford', 'Mustang')
print mustang.wheels
# 4