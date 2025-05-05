#1. Using self
class Student:
    name: str
    marks: int

    def __init__(self, name: str, marks: int) -> str:
        self.name = name
        self.marks = marks

    def display(self) -> str:
        print(f"Name: {self.name}, Marks: {self.marks}")
        
    
student1 = Student("John Doe", 85)

student1.display()


#2. Using cls
class Counter:
    count: int = 0

    def __init__(self) -> None:
        Counter.count += 1

    @classmethod
    def display_count(cls) -> str:
        print(f"Number of Counter objects: {cls.count}")


counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

Counter.display_count()  

#3. Public Variables and Methods

class Car:
    def __init__(self, brand: str) -> None:
        self.brand = brand 

    def start(self) -> str:
        print(f"My {self.brand} car is starting.")

    
car1 = Car("Toyota")
print(f"Car Brand is {car1.brand}")
car1.start()


#4. Class Variables and Class Methods

class Bank:
    bank_name: str = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name: str) -> str:
        cls.bank_name = name
    

bank1 = Bank()
bank2 = Bank()

print(f"Bank Name: {bank1.bank_name}")
print(f"Bank Name: {bank2.bank_name}")

bank1.change_bank_name("XYZ Bank")

print(f"Bank Name: {bank1.bank_name}")
print(f"Bank Name: {bank2.bank_name}")


#5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

print(MathUtils.add(5, 10)) 


#6. Constructors and Destructors
class logger:
    def __init__(self) -> None:
        print("Constructor")

    def __del__(self) -> None:
        print("Destructor.")

log1 = logger()

del log1 


#7. Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name 
        self._salary = salary
        self.__ssn = ssn 

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}") # Access private variable within the class


emp = Employee("Owais Abdullah", 50000, "123-45-6789")

print(f"Name: {emp.name}")  # Public variable we can access directly
print(f"Salary: {emp._salary}")  # Protected variable, Accessible, but python discourages direct access
try:
    print(f"SSN: {emp.__ssn}")  # Private variable, Raises Error, because python name-mangles it
except AttributeError as e:
    print(f"Error: {e}")

emp.display_details()  # Accessing all variables with class method

# Attempting name mangling to access the private variable, as python does not enforce strict access control
# Python uses Name mangling to change the variable name by adding `_ClassName` in the start of the private variable name
print(f"SSN: {emp._Employee__ssn}")  # Accessing the private variable with name mangling


#8. The super() Function
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.subject = subject

    def display(self) -> str:
        print(f"Name: {self.name}, Subject: {self.subject}")

teacher1 = Teacher("Owais", "Mathematics")
teacher1.display()

#9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
    
rectangle1 = Rectangle(5, 10)
print(f"Area of Rectangle: {rectangle1.area()}")

#10. Instance Methods
class Dog:

    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed

    def bark(self) -> str:
        print(f"{self.name} says Woof!")

dog1 = Dog("Tiger", "German Shepherd")
dog1.bark()

# 11. Class Methods
class Books:
    total_books: int = 0

    def __init__(self, title: str) -> None:
        self.title = title
        Books.increment_total_books()

    @classmethod
    def increment_total_books(cls) -> int:
        cls.total_books += 1
        return cls.total_books
    
    @classmethod
    def display_total_books(cls):
        print(f"Total number of books: {cls.total_books}")

book1 = Books("Python Programming")
book2 = Books("Data Science with Python")
book3 = Books("Deep Learning")
book4 = Books("Artificial Intelligence")

Books.display_total_books() 

# 12. Static Methods
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        fahrenheit = f"{celsius} celcius = {(celsius * 9/5) + 32} Fahrenheit"
        return fahrenheit
    

print(TemperatureConverter.celsius_to_fahrenheit(25))

# 13. Composition
class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower
    
class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.engine = Engine(horsepower)
    
    def display(self) -> str:
        print(f"Car Brand: {self.brand}, Horsepower: {self.engine.horsepower}")


car1 = Car("Toyota", 150)

car1.display()


# 14. Aggregation
class Employee:
    def __init__(self, name: str) -> None:
        self.name = name

class Department:
    def __init__(self, name: str, employees: list = None) -> None:
        self.name = name
        self.employees = employees if employees is not None else []

    def __str__(self):
        return f"Department: {self.name}, Employees: {[employee.name for employee in self.employees]}"


employee1 = Employee("John Doe")
employee2 = Employee("Jane Smith")
employee3 = Employee("Alice Johnson")

department1 = Department("HR", [employee1, employee2])
department2 = Department("IT", [employee3]) 
department3 = Department("Finance")

print(department1)
print(department2)
print(department3)

# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self) -> str:
        print("Method from Class A")

class B(A):
    def show(self) -> str:
        print("Method from Class B")


class C(A):
    def show(self) -> str:
        print("Method from Class C")


class D(B, C):
    pass



d = D()
d.show()

print(D.__mro__)

# 16. Function Decorators
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name: str) -> str:
    print(f"Hello, {name}!")

say_hello("Owais")

# 17. Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.greet())

# 18. Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    @price.deleter
    def price(self) -> None:
        del self._price
        print("Price deleted")

product1 = Product("Laptop", 100000)
print(f"Product Name: {product1.name}, Price: {product1.price}")
product1.price = 90000
print(f"Updated Price: {product1.price}")

del product1.price

# print(f"Product Name: {product1.name}, Price: {product1.price}")

# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor: int) -> None:
        self.factor = factor

    def __call__(self, number: int) -> int:
        return number * self.factor
    
multiply_by_2 = Multiplier(2)

callable_result = callable(multiply_by_2)
print(f"Is callable: {callable_result}")

result = multiply_by_2(5)
print(f"Result of multiplication: {result}")

# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)
    
def check_age(age: int) -> None:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older!")
    else:
        print(f"Valid age: {age}")

try:
    age = 10
    check_age(age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e.message}")


# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self) -> int:
        if self.current > 0:
            current_value = self.current
            self.current -= 1
            return current_value
        elif self.current == 0:
            current_value = self.current
            self.current -= 1
            return current_value
        else:
            raise StopIteration
        
countdown = Countdown(5)
for number in countdown:
    print(number)