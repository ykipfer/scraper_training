import time


# Exercise 1

# Decorator that measures how long a function takes to run.
def measure_time(func):
    def wrapper():
        start = time.time()
        result = func()
        time.sleep(2.7)
        end = time.time()
        print(f"Task took approximately {round(end - start, 2)} seconds to finish")
        return result

    return wrapper


@measure_time
def my_function():
    print("I am running some task.")


# Exercise 2
class MyClass:

    @staticmethod
    def sum_function(a, b):
        result = a + b
        return f"{a} + {b} = {result}"


# Exercise 3
def repeat(n_iterations):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n_iterations):
                func(*args, **kwargs)

        return wrapper

    return my_decorator


@repeat(n_iterations=3)
def say_hello(name):
    print(f'Hello my name is: {name}!')


if __name__ == "__main__":
    # Exercise 1
    print("\nEXERCISE 1")
    my_function()

    # Exercise 2
    print("\nEXERCISE 2")
    print(MyClass.sum_function(1, 2))

    # Exercise 3
    print("\nEXERCISE 3")
    say_hello("John")
