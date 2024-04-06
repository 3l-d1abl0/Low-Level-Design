Idea behind Builder pattern is to "Seperate the construction of complex Object from its representation so that the same construction process can create different representations"


This pattern is oftern used with the following GoF Patterns:


1. Composite Patter when you are creating tree-like aggreagations of Objects.

2. Ofter times you will implement your builder pattern as a Singleton.


When to Use Builder Pattern:

1. When you have a complex class with many constructors.
2. When you have to build complex composite tree Objects
3. When you want to build diffrent representations of your complex Object but still use the same general steps.


When no to use:
1. for simplke Objects. can use Factory for that.




Pros of Builder pattern:

1. Provides clear separation between the construction and representation of an Object.
2. Provides finer control over the steps of the construction Process.
3. It supports changing the internal representation of Objects.


Cons:
1. A distinct Concrete Builder must be created for each type of Object.

2. Builder classes must be mutable  .

3. may hamper/complicate dependency injection.



Design Consideration:

1. Builder - encapsulates creation and assembling parts of complex object in a separate Builder Object.

2. Director - delegates object creation to a Builer Object instaead of creating the objects directly.
