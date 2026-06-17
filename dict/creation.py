legend_ipl = dict({'team':'MI','name':'RS'})
print(legend_ipl)

# or

teams = ['Mi', 'Csk', 'kkr']
players = [2, 4, 6]
ipl_legends = dict.fromkeys(teams, players)
print(ipl_legends)
# {'Mi': ['Rs', 'msd', 'narine'], 'Csk': ['Rs', 'msd', 'narine'], 'kkr': ['Rs', 'msd', 'narine']}
