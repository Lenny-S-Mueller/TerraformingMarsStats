from fastapi import FastAPI

import sqlite3

from statistics_db import get_connection, get_player_stats, get_elo_history, get_corporations, get_h2h
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Backend läuft"
    }

@app.get("/players")
def get_players():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM player_statistics
        """
    )


    players = cursor.fetchall()


    connection.close()


    return [
        dict(player) for player in players
    ]

@app.get("/players/{name}")
def get_player(name: str):

    player = get_player_stats(name)

    elo = get_elo_history(name)

    corporations = get_corporations(name)
    
    h2h = get_h2h()


    return {
        "player": player,
        "elo": elo,
        "factions": corporations,
        "h2h": h2h
    }

@app.get("/factions")
def get_factions():

    connection = get_connection()
    
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT *
        FROM faction_games
        GROUP BY faction
        ORDER BY games DESC
    """)

    results = cursor.fetchall()

    connection.close()

    return results

@app.get("/games")
def get_games():

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
    ORDER BY g.game_id DESC, gp.total DESC
    """)    

    rows = cursor.fetchall()

    return rows