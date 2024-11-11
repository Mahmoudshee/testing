import math
import random

def calc (x,y):
    square = math.pi * x**y
    return square

def squareroo (z):
    calc = math.sqrt(z)
    return calc

def guessing ():
    trial = 3
    starting = 1
    random_integer = random.randint(1, 3) 
    while starting <= trial:
        guess = int(input('Guess the number: '))
        if guess == random_integer:
            print('You won!!')
            break
        else:
            print(f"try again ")
            starting += 1
    if starting > trial:
        print(f'you trials are done you limit of trials reached {starting} +254723980834 pastor thuku')

        
    