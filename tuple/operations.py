tuple2 = ('tuple', )
tuple3 = ('tuple',)
tuple4 = ('qwe', 2, 'efw', 56, True)


print(tuple2)
print(tuple3)

# ('tuple',)
# ('tuple',)

tuple5 = tuple4 + tuple2
print(tuple5)
# ('qwe', 2, 'efw', 56, True, 'tuple')

del tuple5
print(tuple5)
# name 'tuple5' is not defined. Did you mean: 'tuple2'?

