Adapter Pattern is used whene there is Interface incompatibility between two exisitng classes.


For Eaxample:

There is a data source which provides data in csv.
And there is an Visuallization class which takes json data and draw visualization in it.

Now in order for both classes to be able to use each other. We need an adapater class between the Two which can take the csv data and Provide it with JSON data.
