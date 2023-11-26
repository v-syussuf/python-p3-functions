#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name = "Naureen"):
    print(f"Hello, ${name}!")

def greet_with_default(name="programmer"):
   print(f"Hello, ${name}!")

greet_with_default("Sunny")   

def add(num1, num2):
    result = num1 + num2
    return result

def halve(number):
    result = number / 2
    return result