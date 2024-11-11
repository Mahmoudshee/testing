import math
import random

def calc1 (x,y):
    math1 = math.pi * x **y
    return math1

def calc2 (q):
    math2 = math.sqrt(q)
    return math2




def guessing_game():
    trial = 3
    starting = 1
    gues_no = random.randint(1,3)
    while starting <= trial:
        guess = input('Guess the number: ')
        if guess == gues_no:
            print('You won!!')
            break
        else:
            print(f"try again ")
            starting += 1
    if starting > trial:
        print(f'you trials are done you limit of trials reached {starting} ')

