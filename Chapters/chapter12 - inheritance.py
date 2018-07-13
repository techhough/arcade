class Boat(): #parent class

    def __init__(self):
        self.tonnage = 0
        self.name = ""
        self.isDocked = True

    def dock(self):
        if self.isDocked:
            print("You are already docked")
        else:
            self.isDocked = True
            print("Docking")

    def undock(self):
        if not self.isDocked:
            print("You aren't docked")
        else:
            self.isDocked = False
            print("Undocking")

class Submarine(Boat): #Submarine is a child class of Boat. Includes all the methods of Boat plus submerge
    def submerge(self):
        print("Submerge!")


enterprise2=Boat()
enterprise2.name="Enterprise II"
enterprise2.tonnage=25

enterprise3=Boat()
enterprise3.name="Enterprise III"
enterprise3.tonnage=135

b = Boat()

b.dock()
b.undock()
b.undock()
b.dock()
b.dock()