import sqlite3


DATABASE = "statistics.db"


def get_connection():

    connection = sqlite3.connect(
        DATABASE
    )
    connection.row_factory = sqlite3.Row

    return connection

def add_rank(players, field, rank_name):
    ranking = sorted(
        players,
        key=lambda p: p[field],
        reverse=True
    )

    current_rank = 1
    last_value = None

    for i, player in enumerate(ranking):

        if player[field] != last_value:
            current_rank = i + 1
            last_value = player[field]

        player[rank_name] = current_rank


def get_player_stats(name):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM player_statistics
        """,
    )


    players = [dict(row) for row in cursor.fetchall()]

    add_rank(players, "current_elo", "elo_rank")
    add_rank(players, "games", "games_rank")
    add_rank(players, "wins", "wins_rank")
    add_rank(players, "ratio", "win_rate_rank")
    add_rank(players, "avg_performance", "perf_rank")

    connection.close()

    print(type(players[0]))
    print(players[0])

    player = next(
    p for p in players
    if p["player"] == name
    )
    
    return player

def get_elo_history(name):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        f'''
        SELECT date, elo
        FROM elo_history
        WHERE player = ?
        ''',
        (name,)
    )

    result = cursor.fetchall()

    connection.close()

    return [dict(row) for row in result]

def get_corporations(name):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT faction,
        COUNT(*) AS times_played,
        SUM(win) as wins
        FROM played_factions
        WHERE player = ?
        GROUP BY faction
        ORDER BY times_played DESC;
        """,
        (name,)
    )

    factions = cursor.fetchall()

    connection.close()

    return [
        dict(row)
        for row in factions
        ]

def get_h2h():
    
    
    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM player_comp
        """
    )


    result = cursor.fetchall()

    connection.close()

    return [dict(row) for row in result]