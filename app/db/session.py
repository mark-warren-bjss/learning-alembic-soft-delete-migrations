from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url = 'postgresql+psycopg2://dev:dev123@localhost:5433/VANISH'
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
