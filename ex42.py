## Animal is-a object (yes, sorf of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## name is-a instance variable
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## name is-a instance variable
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## name is-a instance variable
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## use super() to call the __init__() of the Person class
        ## the first parameter is the subclass, and the second is 
        ## an object that is an instance of the subclass
        super(Employee, self).__init__(name)
        ## salary is-a instance variable
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## saton is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet which is satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet which is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
