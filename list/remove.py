list = [1, 2, 3, 3, 4, 5]


list.remove(1)
print(list)
# [2, 3, 3, 4, 5] removes 1 and only its first occurence


list.pop(2)
print(list)
# # [2, 3, 4, 5]  removes index "2"

i = list.pop(2)
print(i)
print(list)
# 4
# [2, 3, 5]

list.clear()
print(list)
# []
