from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Deliveries(Base):
    __tablename__ = "deliveries"
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.match_id'))
    inning = Column(Integer)
    batting_team = Column(String)
    bowling_team = Column(String)
    over = Column(Integer)
    ball = Column(Integer)
    batsman = Column(String)
    non_striker = Column(String)
    bowler = Column(String)
    is_super_over = Column(Integer)
    wide_runs = Column(Integer)
    bye_runs = Column(Integer)
    legbye_runs = Column(Integer)
    noball_runs = Column(Integer)
    penalty_runs = Column(Integer)
    batsman_runs = Column(Integer)
    extra_runs = Column(Integer)
    total_runs = Column(Integer)
    player_dismissed = Column(String)
    dismissal_kind = Column(String)
    fielder = Column(String)

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, unique=True)
    season = Column(Integer)
    city = Column(String)
    date = Column(String)
    team1 = Column(String)
    team2 = Column(String)
    toss_winner = Column(String)
    toss_decision = Column(String)
    result = Column(String)
    dl_applied = Column(Integer)
    winner = Column(String)
    win_by_runs = Column(Integer)
    win_by_wickets = Column(Integer)
    player_of_match = Column(String)
    venue = Column(String)
    umpire1 = Column(String)
    umpire2 = Column(String)
    umpire3 = Column(String)  # Note: You had duplicate column names, so I added a new one

class Umpire(Base):
    __tablename__ = 'umpires'
    id = Column(Integer, primary_key=True)
    umpire = Column(String)
    country = Column(String)


def create_tables(database_name):
    engine = create_engine(f"postgresql://postgres:123@localhost/{database_name}", echo=True)
    Base.metadata.create_all(engine)