from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Child, Disease, Appointment  # Import your models

DATABASE_URL = "sqlite:///immunization_schedule.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    # This will create all tables defined by the models
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()  # Call this to create the tables when you run this file
