my_dict = {"name":"kenty","age":21}
new_dict = my_dict.copy()
# print(new_dict)

keys = ["name","age","nation"]
# values = "kenty"
final = dict.fromkeys(keys)
# print(final)

new = my_dict.pop("name")
# print(new)
final_dic = {"name":"kenty","age":21,"country":"kenya"}
item = final_dic.items()
key1 = final_dic.keys()
value1 = final_dic.values()

# print(item)
# print(key1)
# print(value1)

value = final_dic.popitem()
# print(value) 

default = final_dic.setdefault("age","muslim")
# print(default)

new_dict = {"name":"raani","age":22}
final_dic.update(new_dict)
# print(final_dic)

key3 = ["country","job"]
value3 = ["India","Dentist"]
final_part = dict(zip(key3,value3))
print(final_part)