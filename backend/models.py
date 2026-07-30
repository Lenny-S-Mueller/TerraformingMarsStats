from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Player(Base):

    __tablename__ = "players"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    games = relationship(
        "GamePlayer",
        back_populates="player"
    )

class Corporation(Base):

    __tablename__ = "corporations"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    games = relationship(
        "GamePlayer",
        back_populates="corporation"
    )


class Game(Base):

    __tablename__ = "games"

    id = Column(
        Integer,
        primary_key=True
    )

    date = Column(
        String,
        nullable=False
    )

    players = relationship(
        "GamePlayer",
        back_populates="game"
    )


class GamePlayer(Base):

    __tablename__ = "game_players"

    id = Column(
        Integer,
        primary_key=True
    )

    game_id = Column(
        Integer,
        ForeignKey("games.id")
    )

    player_id = Column(
        Integer,
        ForeignKey("players.id")
    )

    corporation_id = Column(
        Integer,
        ForeignKey("corporations.id")
    )


    # Statistiken aus Excel

    tf_rating = Column(
        Integer
    )

    awards = Column(
        Integer
    )

    milestones = Column(
        Integer
    )

    greenery = Column(
        Integer
    )

    cities = Column(
        Integer
    )

    victory_points = Column(
        Integer
    )

    total_score = Column(
        Integer
    )

    money = Column(
        Integer
    )


    # Beziehungen

    game = relationship(
        "Game",
        back_populates="players"
    )

    player = relationship(
        "Player",
        back_populates="games"
    )

    corporation = relationship(
        "Corporation",
        back_populates="games"
    )