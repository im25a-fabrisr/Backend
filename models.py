from sqlalchemy import Column, Integer, String, DateTime, Text
from database import Base

class Aufgabe(Base):
    __tablename__ = "Aufgabe"

    AufgabeID = Column(Integer, primary_key=True, index=True)
    Titel = Column(String(100))
    Beginn = Column(DateTime)
    Ende = Column(DateTime)
    Ort = Column(String(250))
    Koordinaten = Column(String(100))
    Notiz = Column(Text)
    KategorieID = Column(Integer)
    PrioritaetID = Column(Integer)
    FortschrittID = Column(Integer)
    BenutzerID = Column(Integer)