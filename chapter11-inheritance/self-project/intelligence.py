"""
Advanced Object System – Animals, Vectors & Employee Intelligence

🎯 Project Objective:
You’ll build a Python program that includes:

A vector algebra system with 2D, 3D, and N-dimensional support

An Animal–Pets–Dog class hierarchy with specific methods

An Employee system with automatic increment adjustments based on salary

Use of operator overloading, @property, and special methods like __str__ and __len__

🔧 Project Structure:
🔹 Part 1: Vector System
Vector2D → basic 2D vector

Vector3D → inherits Vector2D and adds z dimension

VectorND → N-dimensional vector with:

+ overloaded for vector addition

* overloaded for dot product

__len__() → returns the dimension

__str__() → prints nicely like 7i + 8j + 10k

🔹 Part 2: Animal Inheritance
Animal → Pets → Dog

Dog has a method bark() that says "Woof! Woof!"

🔹 Part 3: Employee Increment System
Class Employee

Attributes: salary, increment

@property salary_after_increment

@salary_after_increment.setter → adjusts increment based on salary


"""

import math

# -------------------- VECTOR SYSTEM --------------------

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

class VectorND:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Dimension mismatch")
        result = [a + b for a, b in zip(self.components, other.components)]
        return VectorND(result)

    def __mul__(self, other):  # dot product
        if len(self.components) != len(other.components):
            raise ValueError("Dimension mismatch")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __len__(self):
        return len(self.components)

    def __str__(self):
        symbols = ['i', 'j', 'k']
        terms = []
        for i, val in enumerate(self.components):
            if i < 3:
                terms.append(f"{val}{symbols[i]}")
            else:
                terms.append(f"{val}u{i+1}")
        return " + ".join(terms)


# -------------------- ANIMAL INHERITANCE SYSTEM --------------------

class Animal:
    def sound(self):
        return "Generic animal sound"

class Pets(Animal):
    def friendly(self):
        return "I'm a friendly pet!"

class Dog(Pets):
    def bark(self):
        return "Woof! Woof!"


# -------------------- EMPLOYEE SYSTEM --------------------

class Employee:
    def __init__(self, salary):
        self.salary = salary
        self._increment = 1.1

    @property
    def salary_after_increment(self):
        return self.salary * self._increment

    @salary_after_increment.setter
    def salary_after_increment(self, value):
        self._increment = value / self.salary


# -------------------- DEMO --------------------

print("✅ VECTOR SYSTEM DEMO")
v3 = Vector3D(7, 8, 10)
print("3D Vector:", v3)

v1 = VectorND([1, 2, 3])
v2 = VectorND([4, 5, 6])
v_sum = v1 + v2
v_dot = v1 * v2
print("N-D Vector Sum:", v_sum)
print("N-D Dot Product:", v_dot)
print("Vector Dimension:", len(v1))

print("\n✅ ANIMAL INHERITANCE DEMO")
dog = Dog()
print(dog.sound())
print(dog.friendly())
print(dog.bark())

print("\n✅ EMPLOYEE SYSTEM DEMO")
emp = Employee(50000)
print("Initial salary:", emp.salary)
print("Salary after increment:", emp.salary_after_increment)
emp.salary_after_increment = 60000  # sets new increment
print("Updated increment factor:", round(emp._increment, 2))
print("New salary after increment:", emp.salary_after_increment)
