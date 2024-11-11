#Assertion - > statement that check or test if a condition in your codebase is "true" and if it is not "False"

def avg(mark):

    assert len(mark) != 0,"bro add something in your list"
    return sum(mark) / len(mark)

result = [11,22,42]
result1 = []
print("The result of the avg is : ",avg(result1))
