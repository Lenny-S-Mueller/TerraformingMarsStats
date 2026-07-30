import sqlite3
import numpy as np


connection = sqlite3.connect(
    "games.db"
)

cursor = connection.cursor()

datum = "Lenny"
print("Spiele:")
cursor.execute("""
    SELECT
        g.id,
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
        ON g.id = gp.game_id
    ORDER BY g.date DESC, gp.total DESC
""")

rows = cursor.fetchall()

print(rows)



# print("\nSpielergebnisse:")
# cursor.execute(
#     "SELECT * FROM players LIMIT 10"
# )

# for row in cursor.fetchall():
#     print(row)