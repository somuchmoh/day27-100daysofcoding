# Unlimited positional arguments
def add(*args):
    k = 0
    for n in args:
        k += n
    return k


total = add(1, 2, 3, 4, 5)
print(total)


# Unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

# Creating a class with **kwargs
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")  # This will return none if the keyword is empty


car = Car(make="Toyota", model="Corolla")
print(car.model)

car_new = Car(make="Nissan")
print(car_new.model)