coder = {
    'name': 'Pk2007',
    'age': 19,
    'lang': ['JS', 'Css', 'HTML']
    }

languages_learnt = coder.pop('lang')
print(languages_learnt)
# ['JS', 'Css', 'HTML'] // list returned

coder.popitem()
print(coder)
# {'name': 'Pk2007'} //removed value of age thus removed age key as well


