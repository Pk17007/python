list = ['a', 'b', 'c', 'e']

list_str = ' | '.join(list)
print(list_str)
# a | b | c | e // add any string between

list_str = list_str.split(' | ')
print(list_str)
# ['a', 'b', 'c', 'e']  // remove common string 

print(list[0]*8)
# aaaaaaaa

print([list[0]]*8)
# ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

