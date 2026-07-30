import json
import os
import sqlite3

from statistics_db import (
    get_connection,
    get_player_stats,
    get_elo_history,
    get_corporations,
    get_h2h
)


OUTPUT_DIR = "../data"


def save_json(path, data):

    filepath = os.path.join(
        OUTPUT_DIR,
        path
    )

    os.makedirs(
        os.path.dirname(filepath),
        exist_ok=True
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )

    print("✓", path)



# -------------------------------
# Players Übersicht
# -------------------------------

def export_players():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM player_statistics
    """)

    players = [
        dict(row)
        for row in cursor.fetchall()
    ]

    connection.close()


    save_json(
        "players.json",
        players
    )



# -------------------------------
# Player Details
# -------------------------------

def export_player_details():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""
        SELECT player
        FROM player_statistics
    """)


    names = [
        row["player"]
        for row in cursor.fetchall()
    ]

    connection.close()



    for name in names:


        data = {

            "player":
                get_player_stats(name),

            "elo":
                get_elo_history(name),

            "factions":
                get_corporations(name),

            "h2h":
                get_h2h()

        }


        save_json(
            f"players/{name}.json",
            data
        )



# -------------------------------
# Factions
# -------------------------------

def export_factions():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""
        SELECT *
        FROM faction_games
        GROUP BY faction
        ORDER BY games DESC
    """)


    factions = [
        dict(row)
        for row in cursor.fetchall()
    ]


    connection.close()


    save_json(
        "factions.json",
        factions
    )



# -------------------------------
# Games
# -------------------------------

def export_games():

    connection = sqlite3.connect(
        "games.db"
    )

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()


    cursor.execute("""
        SELECT

        g.game_id,
        g.date,

        gp.player,
        gp.faction,

        gp.tf_rating,
        gp.awards,
        gp.milestones,

        gp.greenery,
        gp.city,

        gp.victory_points,
        gp.total,

        gp.money


        FROM games g

        JOIN game_players gp

        ON g.game_id = gp.game_id


        ORDER BY
        g.game_id DESC,
        gp.total DESC

    """)


    games = [
        dict(row)
        for row in cursor.fetchall()
    ]


    connection.close()


    save_json(
        "games.json",
        games
    )



# -------------------------------
# MAIN
# -------------------------------

if __name__ == "__main__":


    print("\nExport startet...\n")


    export_players()

    export_player_details()

    export_factions()

    export_games()


    print("\n✅ Fertig")