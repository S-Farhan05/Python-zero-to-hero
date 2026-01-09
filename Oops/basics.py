class Dog():
    species="Mammal"
    def __init__(self ,name ,type ,color):
        self.name = name
        self.type = type
        self.color = color

my_dog = Dog("Buddy", "Golden Retriever", "Golden")
print(type(Dog))
print(type(my_dog))

print(my_dog.name)
print(my_dog.species)

## Attributes those were



### Class Attributes and Methods ###

class Circle():

    pie = 3.14

    def __init__(self , radius = 1):
        self.radius= radius
        self.area = radius*radius*Circle.pie
    
    def circumference(self,color):
        self.huh = color
        return 2*self.pie*self.radius
    

my_circle = Circle(radius=21)

print(my_circle.pie)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.circumference(color=10))