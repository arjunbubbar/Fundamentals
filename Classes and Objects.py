class Furniture:
    # Instance variables 
    # Defined with something called a constructor
    # Helps initialise properties of object
    def __init__ (self,material,colour):
        self.material = material
        self.colour = colour


# Creating objects 

chair = Furniture ("wood","brown")
print (chair.material)

table = Furniture ("metal","silver")
print (table.material)