# inheritance all about linking code bases or structuring the code base

class father ():
    def add(self):
        print("this is the addition block")
        x = int(input("Enter your first nunmber: "))
        y = int(input("Enter your second nunmber: "))
        calc = x + y
        print(calc)

class mother(father):
     def sub(self):
        print("this is the subtraction block")
        z = int(input("Enter your first nunmber: "))
        k = int(input("Enter your second nunmber: "))
        calc1 = z - k
        print(calc1)

class child(mother):
     def div(self):
        print("this is the division block")
        a = int(input("Enter your first nunmber: "))
        b = int(input("Enter your second nunmber: "))
        calc2 = a + b
        print(calc2)

obj = child()
obj.sub()
obj.div()
obj.add()
