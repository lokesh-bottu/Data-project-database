from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from create_table import Deliveries,Match,Umpire
import csv
def load_data(csv_path, model_class, sample_session):
    with open(csv_path, 'r',encoding='latin-1') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data = {key.strip(): value for key, value in row.items()}
            sample_session.add(model_class(**data))
    sample_session.commit()

def insert_data(database_name):
    Base = declarative_base()
    engine = create_engine(f"postgresql://postgres:123@localhost/{database_name}", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    matches_path = '/home/lokesh/Downloads/MB SQL/matches.csv'
    umpires_path = '/home/lokesh/Downloads/MB SQL/umpires.csv'
    deliveries_path= '/home/lokesh/Downloads/MB SQL/deliveries.csv'

    load_data(matches_path, Match, session)
    load_data(umpires_path, Umpire, session)
    load_data(deliveries_path,Deliveries , session)