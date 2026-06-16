#  SET  unordered st of unique elements

set1 = {1, 2, 4}
set2 = {1, 4, 5, 2}

print(set1)

set2a = {1, 2, 4, True, 4}
print(set2)
# {1, 2, 4, 5}  // True treated as 1 and set only identifies unique elements

print(len(set2))
# 4

set3 = {1, 'string', 3, True}
print(set3)
# {1, 3, 'string'} // Unordered


