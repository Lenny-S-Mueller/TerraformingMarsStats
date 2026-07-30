import sqlite3
import pandas as pd


EXCEL_FILE = "TerraformingMarsTotalStats.xlsx"
DATABASE_FILE = "games.db"


def clean(value):
    """
    Ersetzt leere Excel-Zellen durch NULL
    """
    if pd.isna(value):
        return None

    return value


# Datenbank öffnen
connection = sqlite3.connect(DATABASE_FILE)
cursor = connection.cursor()


# Tabellen erzeugen
cursor.execute("""
CREATE TABLE IF NOT EXISTS games (
    game_id INTEGER PRIMARY KEY,
    date TEXT NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS game_players (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    game_id INTEGER NOT NULL,

    player TEXT NOT NULL,
    faction TEXT,

    tf_rating INTEGER,
    awards INTEGER,
    milestones INTEGER,

    greenery INTEGER,
    city INTEGER,

    victory_points INTEGER,
    total INTEGER,

    money INTEGER,

    FOREIGN KEY(game_id)
        REFERENCES games(id)
)
""")


# Excel öffnen
excel = pd.ExcelFile(EXCEL_FILE)


for i, sheet in enumerate(excel.sheet_names):

    print(f"Importiere Spiel {sheet}")


    df = pd.read_excel(
        EXCEL_FILE,
        sheet_name=sheet
    )


    # Spiel anlegen
    cursor.execute(
        """
        INSERT INTO games(game_id, date)
        VALUES (?, ?)
        """,
        (i, sheet,)
    )


    game_id = cursor.lastrowid


    # Spieler einfügen
    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO game_players(
                game_id,
                player,
                faction,
                tf_rating,
                awards,
                milestones,
                greenery,
                city,
                victory_points,
                total,
                money
            )
            VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                game_id,

                row["players"],
                clean(row["faction"]),

                clean(row["tf-rating"]),
                clean(row["awards"]),
                clean(row["milestones"]),

                clean(row["greenery"]),
                clean(row["city"]),

                clean(row["Victory-points"]),
                clean(row["total"]),

                clean(row["money"])
            )
        )


connection.commit()
connection.close()


print("✅ games.db erfolgreich erstellt")