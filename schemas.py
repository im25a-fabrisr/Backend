from pydantic import BaseModel
from datetime import datetime


# ── Kategorie ──────────────────────────────────────────────────────────────────
class KategorieBase(BaseModel):
    Kategorie: str
    IstAktiv: bool = True

class KategorieCreate(KategorieBase):
    pass

class KategorieUpdate(KategorieBase):
    pass

class KategorieOut(KategorieBase):
    KategorieID: int

    class Config:
        from_attributes = True


# ── Aufgabe (bereits vorhanden, angepasst) ─────────────────────────────────────
class AufgabeCreate(BaseModel):
    Titel: str
    Beginn: datetime
    Ende: datetime | None = None
    Ort: str | None = None
    Koordinaten: str | None = None
    Notiz: str | None = None
    KategorieID: int
    PrioritaetID: int
    FortschrittID: int
    BenutzerID: int
