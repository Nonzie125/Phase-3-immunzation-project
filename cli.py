import click
from sqlalchemy.orm import Session
from database import engine
from models import Child, Disease, Appointment
from database import Base, engine
from models import Child, Disease, Appointment

# Create the tables if they don't exist
Base.metadata.create_all(bind=engine)

session = Session(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('age', type=int)
def add_child(name, age):
    """Add a child to the database."""
    child = Child(name=name, age=age)
    session.add(child)
    session.commit()
    click.echo(f"Child {name} added to the database.")

@cli.command()
@click.argument('disease_name')
@click.argument('vaccine')
@click.argument('age_for_vaccine', type=int)
def add_disease(disease_name, vaccine, age_for_vaccine):
    """Add a disease and its vaccine to the database."""
    disease = Disease(name=disease_name, vaccine=vaccine, age_for_vaccine=age_for_vaccine)
    session.add(disease)
    session.commit()
    click.echo(f"Disease {disease_name} added to the database.")

@cli.command()
@click.argument('child_id', type=int)
def schedule_appointment(child_id):
    """Schedule an appointment for the child based on their age."""
    child = session.query(Child).get(child_id)  # Use child_id from the argument
    if not child:
        click.echo(f"No child found with ID {child_id}")
        return

    diseases = session.query(Disease).filter(Disease.age_for_vaccine <= child.age).all()
    
    if not diseases:
        click.echo(f"No vaccines required for {child.name} at age {child.age}")
        return

    for disease in diseases:
        appointment = Appointment(child=child, disease=disease)
        session.add(appointment)
        click.echo(f"Appointment scheduled for {child.name} for {disease.vaccine}")
    
    session.commit()

if __name__ == "__main__":
    cli()
