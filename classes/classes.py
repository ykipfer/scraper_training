# Exercise 1
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"Woof.")

    def birthday(self):
        self.age += 1
        print("Happy birthday!")


class ServiceDog(Dog):
    def __init__(self, name, breed, age, task):
        super().__init__(name, breed, age)
        self.task = task

    def perform_task(self):
        print(f'{self.name} the {self.breed} is {self.task}')


if __name__ == "__main__":
    # Exercise 1
    print("\nEXERCISE 1")
    my_dog = Dog("Buddy", "German Shepherd", 2)
    my_dog.bark()

    # Exercise 2
    print("\nEXERCISE 2")
    my_dog = Dog("Buddy", "German Shepherd", 2)
    my_dog.birthday()
    print(f'My dog\'s age is now {my_dog.age}')

    # Exercise 3
    print("\nEXERCISE 3")
    service_dog = ServiceDog("Cookie", "Schapendoes", 1, "walking")
    service_dog.perform_task()

