#  Types of lists
list_nums = [ 1, 2, 3, 6, 0]
list_letters = [ "a", 'f', 'o', 'm']
list_num_letter = ['abc', 3, 5, 'a', 'g']
list_list = [[2,3], ['abc','a', 'd'], [ "a", 'f', 'o', 'm']]

list_print_1 = list_nums[:]
print(list_print_1)
# [ 1, 2, 3, 6, 0]

list_print_2 = list_nums[::3]
print(list_print_2)
# [1, 6]  prints every third term // replace with 2 it prints every second number

# Replacing elements

list_num_letter[1] = ["heloo", 'ad']
print(list_num_letter)
# ['abc', ['heloo', 'ad'], 5, 'a', 'g']


