
set1 = {1, 2, 4}
set2 = {1, 4, 5, 2}
set3 = {1, 'string', 3, True}

# Union
union1 = set1.union(set3)
union2 = set3 | set1
print(union1)
print(union2)
# {1, 2, 3, 4, 'string'}
# {1, 2, 3, 4, 'string'}

# Intersection

inter1 = set1.intersection(set3)
inter2 = set1 & set3
print(inter1)
print(inter2)
# {1}

# Difference

diff1 = set3.difference(set1)
diff2 = set3 - set1
print(diff1) 
print(diff2) 
# {'string', 3}

# 
