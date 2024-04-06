## Singleton Pattern

Singleton Pattern ensures that a Class has only one instance, and provide a global point of access to it.

The Borg (aka monostate Pattern) lets a class have as many instances as one likes, but ensures that they all share the same state.

Singleton pattern ensures that a class has only one instance,
and provide a global access to it. eg. logger
uses __new__ => called before __init__ and responsible for returning
a new instance of your class


The Borg Idiom lets a class ahve as many instances as one like,
but ensures that they all share the same state.
uses __init__ => doesn't return anything , only responsible for
initalizing the instance after its been created.
