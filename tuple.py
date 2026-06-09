tup = (1,2,3,4,5,2)
tup2 = (1)
print(type(tup),type(tup2))
# <class 'tuple'> <class 'int'>

#WAP to count no of students with A grade
# Store below grades in a list and sort them form A to D
grades = ["C","D","A","A","B","B","A","C"]
print("A grade is given to",grades.count("A"),"students")
i = 0
grades.sort()
print(grades)