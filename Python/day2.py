my_list = [1,2,3,4,9,5,6]
my_list.append(7)
my_list.extend([9,10])
my_list.insert(4,9)
my_list.remove(9)
my_list.pop(3)
test = my_list[6]
test2 = my_list.count(9)
my_list.reverse()
my_list.sort()
new_list = my_list.copy()
length = len(new_list)
min = min(my_list)
max = max(my_list)
concat = new_list + [20,30,40,50]
checking = 6 not in my_list
slicing1 = my_list[:]
slicing2 = my_list[::-1]
# del my_list[6]
my_list.clear()
print(my_list)

# print(min,",",max)
# print(concat)
# print(checking)
# print(test)
# print("repeated value is : " ,test2)

