from statistics_db import get_connection
import numpy as np
import pandas as pd



df = pd.read_excel("TerraformingMarsTotalStats.xlsx", sheet_name=None)

def didWin(df, player):
    if player in list(df['players']):
        who = np.where(df['players'] == player)[0][0]
        if len(np.where(df['total'] ==df['total'].max())[0]) == 1:
            return (int(df['total'][who]) == int(df['total'].max()))
        else:
            try:
                return (int(df['money'][who]) == int(df['money'].max()))
            except:
                return False
    else:
        return False
    
def update_elo(plist, data, players):
    h2h = np.zeros((len(plist), len(plist)))
    data = data['total']
    for i, p1 in enumerate(plist):
        for j, p2 in enumerate(plist):
            if i == j:
                h2h[i, j] = 0
            else:
                h2h[i, j] = 1/(1 + 10**((players[p2].elo[-1] - players[p1].elo[-1])/400))
    e_value = h2h.mean(axis = 1) * (2 / (len(plist) - 1))
    e_value = 1/2 * (1 + np.tanh(1 * (e_value - 1/len(plist))))
    actual_score = np.linspace(1, 0, len(plist))
    for i, player in enumerate(plist):
        kfactor = np.heaviside(21 - len(players[player].elo), 0) * (21 - np.sum(players[player].played_game)) + 20
        kfactor = 20
        new_elo = 3 * int((data[i] - np.median(data)) / (np.median(data)*0.1)) + players[player].elo[-1] + kfactor * np.sinh(2 * (actual_score[i] - e_value[i]))#(2*(actual_score[i] - e_value[i]))**3 # (actual_score[i] - e_value[i])#
        players[player].elo.append(int(new_elo))
    
    for player in players:
        if player not in plist:
            players[player].elo.append(players[player].elo[-1])

class Player:
    def __init__(self, name : str):
        self.name = name
        self.games = 0
        self.wins = 0
        self.ratio = 0 
        self.elo = [1000]
        self.avg_perf = []
        self.played_factions = {}
        self.played_game = []
    


players = {
    'Anton' : Player("Anton"),
    'Lars' : Player("Lars"),
    'Lenny' : Player("Lenny"),
    'Maik' : Player("Maik"),
    'Matteo': Player("Matteo")
    }
playerlist = {
    'Anton' : 0,
    'Lars' : 1,
    'Lenny' : 2,
    'Maik' : 3,
    'Matteo' : 4
}
p_comp = np.zeros((5, 5))

for sheet in df:
    data = df[sheet]
    plist = list(data['players'])
    for play in players:
        if play in plist:
           players[play].played_game.append(1)
        else:
            players[play].played_game.append(0)
    mean = data['total'].mean()
    
    update_elo(plist, data, players)

    for i, p1 in enumerate(plist):
        for j, p2 in enumerate(plist):
            if i == j:
                continue
            else:
                p_comp[playerlist[p1], playerlist[p2]] += i - j

    for name in plist:
        
        players[name].games += 1
        if didWin(data, name):
            players[name].wins += 1
        players[name].ratio = np.round(players[name].wins / players[name].games, 3)
        
        pindex = np.where(np.array(plist) == name)[0][0]
        players[name].avg_perf.append(data['total'][pindex] / mean)
        pfac = data['faction'][pindex]
        if pfac in players[name].played_factions.keys():

            players[name].played_factions[pfac] += 1

        else:
            
            if type(pfac) == str:

                players[name].played_factions[pfac] = 1
            

for namee in players.keys():
    players[namee].avg_perf = np.round(np.array(players[namee].avg_perf).mean(), 3)


faction_list = []
for player in players:
    for fac in players[player].played_factions:
        faction_list.append(fac)
fac_list = np.unique(faction_list)

fac_h2h = np.zeros((len(fac_list), len(fac_list)), dtype = int)
fac_games = np.zeros((len(fac_list), len(fac_list)), dtype= int)
for sheet in df:
    data = df[sheet]
    facs = list(data['faction'])
    for i, f1 in enumerate(fac_list):
        for j, f2 in enumerate(fac_list):
            if f1 in facs and f2 in facs and f1 != f2:
                fac_games[i, j] += 1
                fac_games[j, i] += 1
                fac_h2h[i, j] = np.where(np.array(facs) == f2)[0][0] - np.where(np.array(facs) == f1)[0][0]
                fac_h2h[j, i] = np.where(np.array(facs) == f1)[0][0] - np.where(np.array(facs) == f2)[0][0]

faction_perf = np.zeros(len(fac_list))
fac_game_num = np.zeros(len(fac_list))
faction_wins = np.zeros(len(fac_list))

for sheet in df:
    data = df[sheet]
    facs = list(data['faction'])
    for i, fac in enumerate(facs):
        faction_perf[np.where(fac_list == fac)] += data['total'][i] / data['total'].mean()
        fac_game_num[np.where(fac_list == fac)] += 1
        if i == 0:
            faction_wins[np.where(fac_list == fac)] += 1
faction_perf = faction_perf / fac_game_num

dates = []
for sheet in df:
    dates.append(sheet)

faction_stats = []
for i, faction in enumerate(fac_list): 
    facnum = 0
    for player in players:
        if faction in players[player].played_factions:
            facnum += players[player].played_factions[faction]
    faction_stats.append([faction, facnum, int(faction_wins[i])])
fac_df = pd.DataFrame(faction_stats, columns=['faction', 'games', 'wins'])
            


dataframe = []
for i, name in enumerate(players):
    dataframe.append([i+1, players[name].name, players[name].games, players[name].wins, players[name].ratio, np.round(players[name].avg_perf, 3), players[name].elo[-1]])

player_stats = pd.DataFrame(data = dataframe, columns=['id', 'player', 'games', 'wins', 'ratio', 'avg_performance', 'current_elo'])

elo_history = []
for i in range(1, len(df) + 1):
    for player in players:
        elo_history.append([dates[i-1], player, players[player].elo[i]])
elo_df = pd.DataFrame(data = elo_history, columns= ['date', 'player', 'elo'])


comp_df = pd.DataFrame(data = list(p_comp), index=['Anton', 'Lars', 'Lenny', 'Maik', 'Matteo'], columns=['Anton', 'Lars', 'Lenny', 'Maik', 'Matteo'])


played_faction = []
for sheet in df:
    data = df[sheet]
    plist = list(data['players'])
    for i, player in enumerate(plist):
        played_faction.append([sheet, player, data['faction'][i], data['total'][i] / data['total'].mean(), i==0])
    
played_faction_df = pd.DataFrame(data = played_faction, columns=['date', 'player', 'faction', 'points', 'win'])

fac_h2h_df = pd.DataFrame(data = fac_h2h, index = fac_list, columns=fac_list)

games_list = {}
for i, sheet in enumerate(df):
    sheet_dict = {}
    for j, player in enumerate(df[sheet]['players']):
        sheet_dict[player] = df[sheet].iloc[j][1:]

        
    games_list['game_id'] = i
    games_list['date'] = sheet
    games_list['players'] = sheet_dict



connection = get_connection()


player_stats.to_sql(
    "player_statistics",
    connection,
    if_exists="replace",
    index=False
)

elo_df.to_sql(
    "elo_history",
    connection,
    if_exists="replace",
    index=False
)

comp_df.to_sql(
    "player_comp",
    connection,
    if_exists="replace",
    index = True,
    index_label="player"
)

played_faction_df.to_sql(
    "played_factions",
    connection,
    if_exists="replace",
    index=False
)

fac_h2h_df.to_sql(
    "faction_comparison",
    connection,
    if_exists="replace",
    index = True,
    index_label="faction"
)

fac_df.to_sql(
    "faction_games",
    connection,
    if_exists='replace',
    index = False
)


connection.close()