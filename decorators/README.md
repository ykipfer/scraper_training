# Decorators

A Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions and methods (and possibly classes in a future version). This supports more readable applications of the DecoratorPattern but also other uses as well.

In its simplest form, a decorator is just a function that takes a function as an argument and returns a new function that usually extends or modifies the behavior of the input function. Here's an example:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
```

In the above code, `my_decorator` is a decorator. We are defining a function named `my_decorator` that has a single parameter `func`. Inside `my_decorator`, we define a nested function `wrapper`. The `wrapper` function will print a message, then call `func()`, and print another message. The `my_decorator` function returns this `wrapper` function.

When we call `say_hello = my_decorator(say_hello)`, we are not calling the `say_hello` function, we are replacing the `say_hello` function with the `wrapper` function. So when we call `say_hello()`, we are actually calling `wrapper()`. Inside `wrapper`, we call `say_hello()`. So the output will be:

```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

Python allows us to use the `@` symbol along with the name of the decorator function and place it above the definition of the function to be decorated. This is a more convenient way and is commonly used when applying a decorator. Here's how we can do it:

```python
@my_decorator
def say_hello():
    print("Hello!")
```

The above code is equivalent to `say_hello = my_decorator(say_hello)`.

### Exercise 1: Create a decorator

To start with, try to create a simple decorator that measures the time a function takes to execute. Use the time module for this. The decorator should be applied to a function that simply prints "I am running some task".

### Exercise 2: Apply a built-in decorator

Python has several built-in decorators like @staticmethod, @classmethod, and @property. Try to create a simple class and apply the @staticmethod decorator to one of its methods. Call this method and observe the result.

### Exercise 3: Create a decorator with arguments

Decorators can also take arguments. This adds another layer to the nesting. Create a decorator that takes a number as an argument and runs the decorated function as many times as the number given.

Please feel free to ask me for help or for solutions to these exercises.

**More Information on Decorators: https://realpython.com/primer-on-python-decorators/**