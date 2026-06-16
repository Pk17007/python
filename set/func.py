legend_cricketers = {
    'ST',
    'MSD',
    'RS',
    'VK'
}

for players in legend_cricketers:
    print(players)
# VK
# MSD
# RS
# ST


# To access the set convert to list

players_list = list(legend_cricketers)
players_list.append("kumble")

players_set = set(players_list)
print(players_set)
# {'kumble', 'RS', 'VK', 'ST', 'MSD'} // didnt remember the original order as it is a set