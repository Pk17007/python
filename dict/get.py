dict = { 'key':'value', 'key2':'value2'}

print(dict.get('key'))
print(dict.get('key3'))
# value
# None

print(dict.get('key5',"Not founded "))
# Not founded 