# Q: What is the output of the following code?
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
area = rect.calculate_area()
print(area)

# Q: What is the output of the following code?
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers if num % 2 == 0]
print(squared_numbers)


# Q: What is the output of the following code?
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)

# Q: What is the output of the following code?
import re

text = "The cat and the hat sat on the mat."
matches = re.findall(r"[ct]at", text)

print(len(matches))

# Q: What is the output of the following code?
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

# Q: What is the output of the following code?
def uppercase_decorator(func):
    def wrapper(text):
        result = func(text)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

message = greet("John")
print(message)

# Q: What is the output of the following code?
import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)

data["age"] += 1
data["city"] = "San Francisco"

json_string = json.dumps(data)
print(json_string)


# Q: What is the output of the following code?
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
sequence = [next(fib) for _ in range(10)]

print(sequence)

# Q: What is the output of the following code?
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(transposed_matrix)

# Q: What is the output of the following code?
import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_time)

# Q: What is the output of the following code?
class MyFile:
    def __enter__(self):
        self.file = open("data.txt", "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with MyFile() as file:
    lines = file.readlines()

count = len(lines)
print(count)

# Q: What is the output of the following code?
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in "ABCDE":
        print(letter)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

# Q: What is the output of the following code?
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers, reverse=True)

print(sorted_numbers)

#Context managers
# Q: What is the output of the following code?
class MyFile:
    def __enter__(self):
        self.file = open("data.txt", "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with MyFile() as file:
    lines = file.readlines()

count = len(lines)
print(count)

# Q: What is the output of the following code?
fruits = ["apple", "banana", "cherry", "durian"]
sorted_fruits = sorted(fruits, key=len)

print(sorted_fruits)

# Q: What is the output of the following code? Inheritance
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius**2

shapes = [Rectangle(4, 5), Circle(3)]
total_area = sum(shape.area() for shape in shapes)

print(total_area)

# Q: What is the output of the following code?
with open("data.txt", "r") as file:
    lines = file.readlines()

count = sum(1 for line in lines if line.strip())

print(count)

# Q: What is the output of the following code?
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    rows = list(reader)

header = rows[0]
total_rows = len(rows) - 1
total_columns = len(header)

print(total_rows, total_columns)

# Q: What is the output of the following code?
import unittest

def add(x, y):
    return x + y

class AddTestCase(unittest.TestCase):
    def test_addition(self):
        result = add(3, 4)
        self.assertEqual(result, 7)

unittest.main()

# Q: What is the output of the following code?
from contextlib import contextmanager

@contextmanager
def file_open(filename):
    try:
        file = open(filename, "r")
        yield file
    finally:
        file.close()

with file_open("data.txt") as file:
    lines = file.readlines()

count = len(lines)
print(count)

# Q: What is the output of the following code? Webscraping with beautiful soup
import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.string

print(title)


