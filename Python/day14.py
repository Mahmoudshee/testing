# exception = events detected during execution that interupt the flow of a program

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
except ZeroDivisionError:
    print('do not divide number by zero')

except ValueError as kenty:
    print('divide with only number in the input:',kenty)

else:
    print(result)

finally:
    print('end of code')

