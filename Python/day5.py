my_dict = {"name": "John", "age": 30}

# Remove the key-value pair for 'age'del 
del my_dict["name"]

print(my_dict)

my_dict = {"name": "John", "age": 30}

# Check if the key-value pair ('age', 30) exists
exists = ("age",30) in my_dict.items()

print(exists)  # Output: True

