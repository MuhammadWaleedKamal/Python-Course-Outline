# Object Oriented Programming (OOP)

## Classes and Objects

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"{self.name} is {self.age}")

student = Student("Ali", 22)
student.display()
```

## Attributes

Data in a class.

```python
class Person:
    def __init__(self, name):
        self.name = name  # Instance attribute
    
person = Person("Ali")
print(person.name)  # Ali
```

## Methods

Functions in a class.

```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(5, 3)  # 8
```

## Constructor (__init__)

Initializes object.

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

## Inheritance

Class inherits from another.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
```

## Encapsulation

Hide implementation.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    def get_balance(self):
        return self.__balance
```

## Polymorphism

Same method, different behavior.

```python
class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"
```

## Abstraction

Showing only essential details and hiding implementation complexity.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
```

## Magic Methods

Special methods with double underscores.

```python
class Person:
    def __str__(self):
        return f"Person: {self.name}"
    
    def __len__(self):
        return len(self.name)
```
