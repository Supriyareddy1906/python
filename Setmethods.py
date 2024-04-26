# Creating two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Adding an element to set1
set1.add(5)

# Removing an element from set1
set1.remove(1)

# Checking if an element is in set1
element_in_set1 = 2 in set1

# Checking set length
set1_length = len(set1)

# Clearing set1
set1.clear()

# Copying set2
set1_copy = set2.copy()

# Union of set1 and set2
set_union = set1_copy.union(set2)

# Intersection of set1 and set2
set_intersection = set1_copy.intersection(set2)

# Difference between set1 and set2
set_difference = set1_copy.difference(set2)

# Symmetric difference between set1 and set2
set_symmetric_difference = set1_copy.symmetric_difference(set2)

# Subset check
subset_check = set1_copy.issubset(set2)

# Superset check
superset_check = set1_copy.issuperset(set2)

# Disjoint check
disjoint_check = set1_copy.isdisjoint(set2)

# Removing and returning an arbitrary element from set2
removed_element = set2.pop()

# Printing results
print("Element in set1:", element_in_set1)
print("Length of set1:", set1_length)
print("Cleared set1:", set1)
print("Copied set1:", set1_copy)
print("Union of set1 and set2:", set_union)
print("Intersection of set1 and set2:", set_intersection)
print("Difference between set1 and set2:", set_difference)
print("Symmetric difference between set1 and set2:", set_symmetric_difference)
print("Subset check:", subset_check)
print("Superset check:", superset_check)
print("Disjoint check:", disjoint_check)
print("Removed element from set2:", removed_element)
