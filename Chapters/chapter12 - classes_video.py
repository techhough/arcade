"""
Video content
https://www.youtube.com/watch?v=UvX28buBN3U
"""

class Character(): #name of class
    #list class attributes
    name = "none_defined"
    sex = "none_defined"
    max_hit_points = 50
    current_hit_points = 50
    max_speed = 10
    armour_amount = 8

def display_character(my_character):
    print(my_character.name,
          my_character.sex,
          my_character.max_hit_points,
          my_character.current_hit_points,
          my_character.max_speed,
          my_character.armour_amount)

my_dude=Character() #creates an instance of the class (object 1)

#my_dude is a variable that points to the object, not the object itself

#use dot operator to set object attributes
my_dude.name = "Sally"
my_dude.sex = "female"
my_dude.max_hit_points = 60

his_dude=Character() #object 2
his_dude.name = "Josh" #set object attributes

display_character(my_dude)
display_character(his_dude)