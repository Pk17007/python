#  Types of lists
list_nums = [ 1, 2, 3, 6, 0]
list_letters = [ "a", 'f', 'o', 'm']
list_num_letter = ['abc', 3, 5, 'a', 'g']
list_list = [[2,3], ['abc','a', 'd'], [ "a", 'f', 'o', 'm']]

# one, two, three, six, zero = list_nums
# print(list_nums)
#  [1, 2, 3, 6, 0]

# one, two, three = list_nums
# print(list_nums)
# ValueError: too many values to unpack (expected 3, got 5)

# one, two, three, six, zero, five = list_nums
# print(list_nums)
# ValueError: not enough values to unpack (expected 6, got 5)