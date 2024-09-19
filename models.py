from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Child(Base):
    __tablename__ = 'children'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    # Relationship to appointments
    appointments = relationship("Appointment", back_populates="child")

class Disease(Base):
    __tablename__ = 'diseases'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    vaccine = Column(String, nullable=False)
    age_for_vaccine = Column(Integer, nullable=False)

    # Relationship to appointments
    appointments = relationship("Appointment", back_populates="disease")

class Appointment(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    child_id = Column(Integer, ForeignKey('children.id'), nullable=False)
    disease_id = Column(Integer, ForeignKey('diseases.id'), nullable=False)
    
    child = relationship("Child", back_populates="appointments")
    disease = relationship("Disease", back_populates="appointments")
