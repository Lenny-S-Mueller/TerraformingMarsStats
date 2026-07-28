import sqlite3


connection = sqlite3.connect(
    "statistics.db"
)

cursor = connection.cursor()

datum = "Lenny"
print("Spiele:")
cursor.execute(
    f'''SELECT date, elo FROM elo_history WHERE player = ?'''('Lenny')
)

for row in cursor.fetchall():
    print(row)


# print("\nSpielergebnisse:")
# cursor.execute(
#     "SELECT * FROM players LIMIT 10"
# )

# for row in cursor.fetchall():
#     print(row)