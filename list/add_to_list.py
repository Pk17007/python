list_letter = ['q', 'w', 'r', 'b', 'g']

list_letter.extend(['a', 'b'])
print(list_letter)
# ['q', 'w', 'r', 'b', 'g', 'a', 'b']  // extends the list from end
# OR
list2 = ["c", "A", "g"]
list_letter.extend(list2)
print(list_letter)
# ['q', 'w', 'r', 'b', 'g', 'a', 'b', 'c', 'A', 'g']  // used list2 to extend from end


list_letter = list_letter + ["added"]
print(list_letter)
# ['q', 'w', 'r', 'b', 'g', 'a', 'b', 'c', 'A', 'g', 'added']


list_letter.insert(5,"inserted")
print(list_letter)
# ['q', 'w', 'r', 'b', 'g', 'inserted', 'a', 'b', 'c', 'A', 'g', 'added']
#  Insert element vefore given index  // a is 5 index