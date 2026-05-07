set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference:", set1.difference(set2))

# Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Subset / Superset
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))
print(b.issuperset(a))