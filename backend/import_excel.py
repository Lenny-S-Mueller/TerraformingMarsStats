import pandas as pd

from database import SessionLocal
from models import (
    Player,
    Corporation,
    Game,
    GamePlayer
)


EXCEL_FILE = "TerraformingMarsTotalStats.xlsx"


db = SessionLocal()


excel = pd.ExcelFile(EXCEL_FILE)


for sheet in excel.sheet_names:

    print(f"Importiere Spiel: {sheet}")

    # Datum aus Tabellenblatt
    game = Game(
        date=sheet
    )

    db.add(game)
    db.commit()
    db.refresh(game)


    df = pd.read_excel(
        EXCEL_FILE,
        sheet_name=sheet
    )


    for _, row in df.iterrows():

        player_name = row["players"]
        corporation_name = row["faction"]


        # Spieler suchen oder erstellen
        player = db.query(Player)\
            .filter(Player.name == player_name)\
            .first()


        if not player:
            player = Player(
                name=player_name
            )

            db.add(player)
            db.commit()
            db.refresh(player)



        # Konzern suchen oder erstellen
        corporation = db.query(Corporation)\
            .filter(Corporation.name == corporation_name)\
            .first()


        if not corporation:
            corporation = Corporation(
                name=corporation_name
            )

            db.add(corporation)
            db.commit()
            db.refresh(corporation)



        # Spielergebnis speichern
        game_player = GamePlayer(

            game_id=game.id,

            player_id=player.id,

            corporation_id=corporation.id,

            tf_rating=row["tf-rating"],

            awards=row["awards"],

            milestones=row["milestones"],

            greenery=row["greenery"],

            cities=row["city"],

            victory_points=row["Victory-points"],

            total_score=row["total"],

            money=row["money"]
        )


        db.add(game_player)


    db.commit()


db.close()


print("Import abgeschlossen!")