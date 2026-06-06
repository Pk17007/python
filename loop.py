# WAP to write num and their square 11 24 39 using while
# i = 1
# while i<=10:
#     print(i,i**2)
#     i=i+1

#############################################
# write a reverse series using while
# i=300
# while i>40:
#     print(i)
#     i=i-13
#############################################
# WAP to display table of a User defined num
# i = int(input("Enter a number  "))
# j=1
# while j<=10:
#     print(i,"X",j,"=",i*j)
#     j=j+1
############################################
#WAP to display even no between 2 usedef num
i=int(input("Enter first number "))
j=int(input("Enter second number "))
count = 0 
if i>j:
    while i>j:
        if j%2==0:
            print(j)
            count = count+1
        j=j+1
else:
    while  j>i:
        if i%2==0:
            print(i)
            count = count+1
        i=i+1
print("No. of even numbers",count)
    