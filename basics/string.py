str = "Fruit"
# print(str[0])
# print(str[0:2])
# print(str[1:4])
# print(str[0:-4])
# print(len(str))




# String Methods


# Upper and lower
# print(str.upper())
# # print(str.lower())


# rstrip

# trail = "Heloo!!!oo"
# trail2 = "Heloo!!!"
# trail3 = "Heloo!!!ooo"
# print(trail.rstrip("o"))
# print(trail.rstrip("!"))
# print(trail.rstrip("!","o")) ; TypeError: rstrip expected at most 1 argument, got 2

#################################################
# replace() and split()

# string="abcdefgj"
# string2 = string.replace("j","h")
#print(string2[0:len(string2)-1])

# # print(string.split("d"))

#############################################
# capitalize  cnter 
#More specifically, make the first character have upper case and the rest lower case
# string= "abCedAD"
# print(string.capitalize())  
# output = Abcedad

#Return a centered string of length width.\
# Padding is done using the specified fill character ( )

# string = "abcdefghij"
# print(string.center(60))
# print(string.center(60,'o'))

# Outputs
#                          abcdefghij                         
# oooooooooooooooooooooooooabcdefghijooooooooooooooooooooooooo

###############################################################
# count() # endswith() # find()
string = "anbskibwkwnannfb jefadwebakufcvhjfyaea;c22<"

# print(string.count("w"))
# 3
# print(string.endswith("<"))  
# True
# print(string.endswith("n",10,13))  
#True
# print(string.find("d"))
#20
# print(string.index("-"))
# print(string.find("-"))
#  index = error   find = -1

# print(string.isalnum())
# # false
# print(string.isalpha())
# # false
# print(string.islower())
# True  doesnt check any other datatype accept alpha ones

# print(string.isprintable())
# true  no \n used
# print(string.isspace())  !!!
#false

# print(string.istitle())
# flase

# print(string.swapcase())
# JEFADWEBAKUFCVHJFYAEA;C22<

# print(string.title())
# Anbskibwkwnannfb Jefadwebakufcvhjfyaea;C22<


