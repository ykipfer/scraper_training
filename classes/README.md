# Classes

### Defining a Class

Classes in Python are defined using the `class` keyword, followed by the name of the class (by convention, class names in Python are typically written in CamelCase).

```python
class MyClass:
    pass
```

### Initializing a Class: The `__init__` Method

The `__init__` method is a special method that is automatically called when an object of a class is instantiated. It is typically used to initialize the attributes of a class.

```python
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
```

### Creating an Instance of a Class

An instance of a class (also known as an object) can be created by calling the class as if it were a function, passing any required arguments to the `__init__` method.

```python
my_instance = MyClass("value1", "value2")
```

### Instance Methods

Instance methods are functions that are defined inside a class and can only be called on an instance of that class. The first argument to an instance method is always `self`, which is a reference to the instance of the class.

```python
class MyClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def my_method(self):
        return self.attribute1 + self.attribute2
```

### Inheritance

Inheritance allows one class to inherit the attributes and methods of another class. The class that is being inherited from is called the parent class, and the class that is doing the inheriting is called the child class.

```python
class MyChildClass(MyClass):
    pass
```

In this example, `MyChildClass` will have all the same attributes and methods as `MyClass`.

### Overriding Methods

In a child class, you can override methods from the parent class by defining a method with the same name. The new method in the child class will be used instead of the one in the parent class.

```python
class MyChildClass(MyClass):
    def my_method(self):
        return self.attribute1 * self.attribute2
```

In this example, `my_method` in `MyChildClass` will multiply the attributes together instead of adding them.

These are the main concepts of classes in Python. There are more advanced topics like class methods, static methods, and private methods, but these are the basics.

### Exercises

1. **Create a Class:** Create a class called `Dog`. This class should have an `__init__` method that takes in a name and a breed, which should be saved as attributes. Also, create a method `bark` in the class that prints "Woof!"

2. **Create an Object:** Using your Dog class, create an object. You can give it any name and breed you want. Then, call the `bark` method for your dog.

3. **Adding Attributes:** Modify the `Dog` class to include an age attribute. Add a method `birthday` that increases the age by one and then print a happy birthday message.

4. **Inheritance:** Create a new class called `ServiceDog` that inherits from the `Dog` class. Add an attribute for the task that the service dog performs. Add a method `perform_task` which prints out a message about the task.

5. **Overriding Methods:** In the `ServiceDog` class, override the `bark` method. Instead of just barking, the service dog should also perform its task when it barks.


**More Information on Classes: https://realpython.com/python-classes/**