list_nums = [ 1, 2, 8, 6, 0]
list_letters = [ "a", 'f', 'o', 'm']
list_num_letter = ['abc', 3, 5, 'a', 'g']
list_list = [[2,3], ['abc','a', 'd'], [ "a", 'f', 'o', 'm']]

list_letters.sort()
print(list_letters)
# ['a', 'f', 'm', 'o']
#  OR
i = sorted(list_nums)
print(i)
# [0, 1, 2, 6, 8]  // returns ascending thus catched it in "i"

# Order

list_letters.reverse()
print(list_letters)
# ['o', 'm', 'f', 'a']
# OR
# list_num_letter.sort(reverse=True)
# print(list_num_letter)
# TypeError: '<' not supported between instances of 'int' and 'str'

list_letters.sort(reverse=True)
print(list_letters)
# ['o', 'm', 'f', 'a']