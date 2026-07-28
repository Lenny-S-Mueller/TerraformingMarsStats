from fastapi import FastAPI

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