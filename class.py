class Fruit:

    def __init__(self, color) -> None: 
        self._color = color

    def print(self):
        print ("I am", self.FruitName(), "of color", self._color)

    def FruitName(self):
        pass

class Apple(Fruit): 
    
    # Apple inherits from Fruit
    # Apple is a specialization of the Fruit concept
    # Fruit is a generalization of Apple
    # Attributes and functions of Fruit is a proper subset of Apple
    # All attributes and functions of Fruit is also inherited by Apple
    # Apple is a sub-class of Fruit
    # Fruit is a base class of Apple

    def FruitName(self): 
        # Function override: This function overrides Fruit.FruitName

        return "an apple"

class Banana(Fruit):

    def FruitName(self): #
        return "a banana"

class Orange(Fruit):

    def FruitName(self): #
        return "an orange"


##################################################
# Construction part 

fruits = []
fruits.append(Apple("red"))
fruits.append(Banana("yellow"))
fruits.append(Apple("red"))
fruits.append(Orange("red"))
fruits.append(Apple("green"))
fruits.append(Banana("brow"))



###############################################
# ALgorithm part

# POLYMORPHISM
# Code is written in an abstract manner without caring about specific classes of objects
# But objects behave as their own identity.

for fruit in fruits:
    fruit.print()