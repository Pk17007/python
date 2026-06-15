def sq_class(length):
    area = length**2
    peri = length*4
    return area, peri

result = sq_class(5)

print(result)
print(result[0])
print(result[1])

# (25, 20) // function returns tuple
# 25 // area
# 20 // peri

