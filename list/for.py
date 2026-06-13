list = [1, 2, 3, 4, 5, 6, 7]

for index,nums in enumerate(list):
    print(index, nums)
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6
# 6 7

for index,nums in enumerate(list,start=2):
    print(index, nums)
# 2 1
# 3 2
# 4 3
# 5 4
# 6 5
# 7 6
# 8 7