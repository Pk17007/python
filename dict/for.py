dict = {'key': 'value', 'key2': 'value2'}

for data in dict.values():
    print(data)
    # value
    # value2

for data in dict.keys():
    print(data)
    # key
    # key2

for data in dict.items():
    print(data)
    # ('key', 'value')
    # ('key2', 'value2')

    
for key,value in dict.items():
    print(key, "coresponds", value)
    # key coresponds value
    # key2 coresponds value2
    