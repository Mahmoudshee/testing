# i = 1  

# while i <= 30:  
#     if i == 20:  
#         i += 1  
#         continue  
#     else:
#         print(i)  
#         i += 1  

# for i in range (1,5+1):
#     for j in range (1,5+1):
#         print(f"{i * j :3}", end='')
#     print()
# kenty = 'hello'
# for i in kenty:
#     print(i)





def ending_point(row,cols):
    for i in range(1,cols +1):
        for x in range(1,row +1):
            print(f"{i * x :3}",end='')
        print()
row1 = int(input("Enter the rows: "))
cols1 = int(input("Enter the cols: "))
ending_point(row1,cols1)


# def mathematica (num1,num2): 
#     result = num1 * num2
#     return result
# key1 = int(input("number1: "))
# key2 = int (input("number2: "))
# kenty = mathematica(key1,key2)
# print(kenty)

# Import necessary modules
import math
import random

# Using the math module
# Example: Calculating the square root, factorial, and sine of a number
number = 16
square_root = math.sqrt(number)  # Calculates square root
factorial = math.factorial(5)    # Calculates factorial of 5
sine_value = math.sin(math.radians(30))  # Calculates sine of 30 degrees

print(f"Square root of {number}: {square_root}")
print(f"Factorial of 5: {factorial}")
print(f"Sine of 30 degrees: {sine_value}")

# Using the random module
# Example: Generating random numbers and making a random choice from a list
random_float = random.random()  # Generates a random float between 0 and 1
random_integer = random.randint(1, 100)  # Generates a random integer between 1 and 100
random_choice = random.choice(['apple', 'banana', 'cherry'])  # Randomly chooses an item from the list

print(f"Random float between 0 and 1: {random_float}")
print(f"Random integer between 1 and 100: {random_integer}")
print(f"Random choice from the list: {random_choice}")
