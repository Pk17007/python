set1 = {1, 2, 4}
set2 = {1, 4, 5, 2}
set3 = {'string', 3, True, 2, 4, False,5}
set4 = {0}

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set4))
# False
# True


print(set3.issuperset(set2))
print(set3.issubset(set2))
# True
# False