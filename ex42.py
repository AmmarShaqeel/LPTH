## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## cat has-a name
		self.name = name
	
## Cat is-a Animal
class Cat(Animal):
	
	def __init__(self, name):
		## cat has-a name 
		self.name = name
		

## Person is-a object
class Person(object):

	def __init__(self, name):
		## person has-a name 
		self.name = name
		
		## Person has-a pet of some sort
		self.pet = None
		
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name
		super(Employee, self).__init__ (name)
		
		## Employee has-a salary
		self.salary = salary
	
## Fish is-a object
class Fish(object):
	pass
	
## Salmon is-a fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish
class Halibut(Fish):
	pass
	

## Rover is-a Dog
rover = Dog("Rover")

## Satan is-a cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Frank is-a employee with a salary of 120000
frank = Employee("Frank", 120000)

## Frank has-a pet rover
frank.pet = rover

## flipper is-a instance of  fish
flipper = Fish()

## crouse is-a instance of salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()
