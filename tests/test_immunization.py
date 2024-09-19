import pytest
from sqlalchemy.orm import sessionmaker
from database import engine
from models import Child, Disease, Appointment, Base

Session = sessionmaker(bind=engine)

@pytest.fixture
def session():
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_add_child(session):
    child = Child(name="Alice", age=1)
    session.add(child)
    session.commit()
    
    assert child.id is not None

def test_add_disease(session):
    disease = Disease(name="Polio", vaccine="Polio Vaccine", age_for_vaccine=6)
    session.add(disease)
    session.commit()
    
    assert disease.id is not None

def test_schedule_appointment(session):
    child = Child(name="Alice", age=6)
    disease = Disease(name="Polio", vaccine="Polio Vaccine", age_for_vaccine=6)
    session.add(child)
    session.add(disease)
    session.commit()
    
    appointment = Appointment(child=child, disease=disease)
    session.add(appointment)
    session.commit()

    assert appointment.id is not None
    assert appointment.disease == disease
