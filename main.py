from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas # Meine Dateien
from database import SessionLocal, engine

@app.post("/aufgaben/")
def erstelle_aufgabe(aufgabe: schemas.AufgabeCreate, db: Session = Depends(get_db)):
    passfrom fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas # Meine Dateien
from database import SessionLocal, engine

@app.post("/aufgaben/")
def erstelle_aufgabe(aufgabe: schemas.AufgabeCreate, db: Session = Depends(get_db)):
    pass