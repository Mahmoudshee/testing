set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}


# Add an element to set1
set1.add(8)
print("After adding 8 to set1:", set1)


# Update set1 with elements from set2
set1.update(set2)
print("After updating set1 with set2:", set1)


# Remove an element from set1
set1.remove(2)
print("After removing 2 from set1:", set1)


# Discard an element from set1 (no error if not found)
set1.discard(8)
print("After discarding 8 from set1:", set1)


# Pop an element from set1
popped_element = set1.pop()
print("Popped element from set1:", popped_element)


# Create a copy of set1
set1_copy = set1.copy()
print("Copy of set1:", set1_copy)


# Union of set1 and set2
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)


# Intersection of set1 and set2
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)


# Difference between set1 and set2
difference_set = set1.difference(set2)
print("Difference between set1 and set2:", difference_set)


# Symmetric difference between set1 and set2
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference between set1 and set2:", symmetric_difference_set)


# Check if set2 is a subset of set1
is_subset = set2.issubset(set1)
print("Is set2 a subset of set1?", is_subset)


# Check if set1 is a superset of set2
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)


# Check if set1 and set2 are disjoint
is_disjoint = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?", is_disjoint)