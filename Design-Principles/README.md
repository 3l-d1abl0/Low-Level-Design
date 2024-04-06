# SOLID Design Principles

Design principles are guidelines that helps us to improve our Object-oriented design while creatign Applications. Again these are guidelines and not some hard and fast Rule, they are meant to be taken as Advice. Design Principles can be thought of as Common Sense Rule/ Advisory that have work in several situations and you don't need it always.
They are important because they help us avoid Bad object-oriented Design.
Some properties of Bad Object-oriented Design :
* Rigidity - A system/module is said to be rigid, if its hard to change due to some dependencies. And doing so might lead to a cascade of changes across other part of the Module
* Fragility - Your system might be susceptible to erros/bugs in different unrealted parts of the system if you deploy some changes in the code.
* Immobility - If the code hard to reuse for different Problems as its needs too much modification.


Design principles, they help us by giving us an additional set of guidelines on Top of the core Object-Oriented Concepts :
* Inheritance
* Encapsulation
* Polymorphism
* Abstraction

since blindly following these might lead us to Bad Object Oriented designs. And this is where SOLID Design Principles comes to the rescue as it tells you how to and how not to approach Object-oriented Design. And following these design patterns have resulted in recurring patterns of how we structure the larger object Oriented Designs, which are called Design Patterns.

### Fundamental Principles
* Encapsulate what varies
* Favor composition over inheritance
* Program to interfaces
* Loose coupling
  
* Single Responsibility (S)
* Open/Closed (O)
* Liskov Substitution (L)
* Interface segregation (I)
* Dependency inversion (D)
  
  
Lets take a little closer look at these principles :

### 1. Encapsulate that varies
  It simply says that if there is an aspect of your code that changes with every new Requirement, you need to seperate it from what stays the same. The simple advantage it gives is that you can modify/extend the part which keeps changing without affecting the parts which remains the same.
  consider a pythonic sudo-code:

```Python
	def getCar(car_type):
	    
	    if car_type == 'SEDAN':
	        car = CarSedan
	    elif car_type == 'HATCHBACK'
	        car = CarHatchback
	    else:
	        car = CarConvertible
	        
	        
	    car.paint()
	    car.wash();
	    car.addAccessories();
	    
	    return car
```

As we can notice there are bunch o f if statements, responsible for creation of a car followed by some operation on the car. If new type of car gets added, we might have to aliter the if statements. And if that gets messed up then we have messed teh entire process, some of which were not even varying.
We can encapsulated this code simply by taking out the varying part into another class:

```Python
class CarFactory:
    
    def createCar(type):
        
        if car_type == 'SEDAN':
	        car = CarSedan
	    elif car_type == 'HATCHBACK'
	        car = CarHatchback
	    else:
	        car = CarConvertible
	        
	        
	   return car
```

So, now the task of creating aCar object is handled by a new Class. If any changes need to be made to the car type, it will locallized to that particular class, without affecting rest of the code.
Fun Fact: this is the basis of almost every design pattern


### 2. Favour Composition over Inheritance

	HAS-A better than IS-A ?
This rule simply asks us think if HAS-A (composition) better than IS-A (Inheritance)

Examples of Composition:
* An Account has a transaction history
* A Taxi has a Driver

Example of Inheritance:
* Dog is an Animal
* Eagle is a Bird

Consider a design of a Coffeee Shop with 3 condiments: Mocha, Butter, Milk
[image Here]

What if the the shop need to add new Condiments ?or new Combination of Condiments ?
Do we keep adding new class or creating Combination of Condiments ?
Can we break down this design as Coffee having Condiments i.e. coffee is composed of different Condiments OR coffee HAS-A condiment ?
With this approach we have a Condiment class and Mocha, Butter and Milk are different sub-classes of Condiments.
And Coffee Class is composed of 0 or 1 Condiments class.
[Image Here]

After using composition we can add any number of condiments to our coffee.
Instead of inheriting our behaviour we can compose our object with new behaviours.
Inheritance adds the behaviour at compile time, composition allows behaviour for runtime !




### 3.  Program to interfaces



### 4. Loose coupling



### 5. Single Responsibility Principle

We must have heared of Single Responsibility by many different statements like:
The SRP requires that a class should have only a single responsibility.
Each Software Module(class/function) should have only one and one reason to change.

Simply said a class should have only one job and if a class has more than one responsibility, it becomes tightly coupled. A change to one responsibility might result in the modification of other responsibility.

When designing classes, we shoild aim to put related feature together, so whenever they tend to change, it would be for same reason. And we should try to seperate feature if they will change for different reasons.

Consider a high level view of a Note Talking App, where you add your notes and then save it to the Disk.
```Python

		class Notes:
		
			def __init__(self):
		  
		
			def add_entry(self, text):
		
		
			def save(self, filename):		
		
				file.write()
			

```

The problem with thi sapproach is along with keeping the note entries this also handles the functionality of writing to the disk, now future there might be functionality to encrypt the data before writing it to the Disk or may upload it to any drive before writing it to a Drive etc.
A better idea would be to give the responsibility of persisting the data to another module/class. Somethign like the following :

```Python

	class Notes:

		def __init__(self):
  

		def add_entry(self, text):
	


	class FileSystem:


		def save_to_file(notes, filename):

		#new features like sav to drive can be added furtur
		def save_to_drive(notes, url):

```


### 6. Open Closed Principle

Software enitites (classes, modules etc.) should be open for extension and should be closed for Modification.
Usually for every new requirement the most common approach is to modifiy the existing Code, which can introduce new bugs to the existing code.
Three approaches to achieve OCP.
1. Parameter/Argument : Pass parameter to the function and then keep a check in the function definiton and based of the parameter call relevent method/class.
2. Inheritance/Abstract Class : Keep ans abstract class and when requiremnet comes, create a base class and override the existing function or add new function.
3. Composition/Injection : Keep the logic in other class and keep adding new class with requirement and use them via dependency Injection.


### 7. Liskov's Substitution Principle

Liskov's Substitution Principle simple states that the Sub Classes should be albe to substitute for the Base Classes

"Do your Subclasses behave like you Super Classes ?"

### 8. Interface Segeregation Principle

It states that we should prefer to use Small, Cohesive Interfaces than Large Interfaces.
i.e clients should not be forced to provide the definitions of the methods which they do no use.


### 9. Dependecy Inversion Principle (DIP)

High Level Modules should not depend on Low Level Modules. Both should depend on Abstractions and Abstractions should not depend on details but rather details should depend on abstractions.