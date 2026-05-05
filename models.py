from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Aufgabe(Base):
    __tablename__ = "aufgaben" # Muss exakt wie in MySQL heißen

    id = Column(Integer, primary_key=True, index=True)
    titel = Column(String(100))
    beschreibung = Column(String(255))
    erledigt = Column(Boolean, default=False)