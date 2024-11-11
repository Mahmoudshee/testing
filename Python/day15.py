class kenty:
    def __init__(self,name,street,age):
        self.jina = name
        self.mtaa = street
        self.miaka = age
    def raani(self):
        a = int(input("Enter your first number: "))
        b = int(input("Enter your first number: "))
        result = a / b
        print(result)
        



    
my_object = kenty('mahmoud','maweni',21)
my_object.user = 'Instagram'
print(my_object.user)
print(my_object.jina,my_object.mtaa)

## Now lets call the function by creating an object

obj_1 = kenty('mahmoud','maweni',21)
kenty.raani(obj_1)