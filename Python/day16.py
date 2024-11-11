class MyClass:
    def __init__(self, value):
        self.__private_attribute = value  # Private attribute
    
    def __private_method(self):  # Private method
        print("This is a private method")
    
    def public_method(self):
        print(f"Accessing private attribute: {self.__private_attribute}")
        self.__private_method()  # Accessing private method within the class

# Creating an object
obj = MyClass(42)

# Accessing public method
obj.public_method()

# Trying to access private attribute or method will raise an error
# print(obj.__private_attribute)  # This will raise an AttributeError
# obj.__private_method()  # This will raise an AttributeError

# Private members can still be accessed using name mangling
# print(obj._MyClass__private_attribute)  # This will work, but it's not recommended
