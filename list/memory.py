list_letter = ["a", "b", "c"]
list_letter2 = ["d", "e", "f"]

list_letter2 = list_letter
list_letter[2] = "z"
print(list_letter)
print(list_letter2)
# ['a', 'b', 'z']
# ['a', 'b', 'z'] //

# To avoid this we usee copy statements
list_letter = ["a", "b", "c"]
list_letter3 = list_letter[:]
print(list_letter3)
# ['a', 'b', 'c']
# OR
list_letter4 = list_letter.copy()
print(list_letter4)
# ['a', 'b', 'c']