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


# ── Prioritaet ─────────────────────────────────────────────────────────────────
class PrioritaetBase(BaseModel):
    Prioritaet: str

class PrioritaetCreate(PrioritaetBase):
    pass

class PrioritaetUpdate(PrioritaetBase):
    pass

class PrioritaetOut(PrioritaetBase):
    PrioritaetID: int

    class Config:
        from_attributes = True


# ── Fortschritt ────────────────────────────────────────────────────────────────
class FortschrittBase(BaseModel):
    Fortschritt: str

class FortschrittCreate(FortschrittBase):
    pass

class FortschrittUpdate(FortschrittBase):
    pass

class FortschrittOut(FortschrittBase):
    FortschrittID: int

    class Config:
        from_attributes = True


# ── Benutzer ───────────────────────────────────────────────────────────────────
class BenutzerBase(BaseModel):
    BenutzerName: str

class BenutzerCreate(BenutzerBase):
    BenutzerPWD: str

class BenutzerUpdate(BenutzerBase):
    BenutzerPWD: str

class BenutzerOut(BenutzerBase):
    BenutzerID: int

    class Config:
        from_attributes = True


# ── Material ───────────────────────────────────────────────────────────────────
class MaterialBase(BaseModel):
    Material: str
    IstAktiv: bool = True

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(MaterialBase):
    pass

class MaterialOut(MaterialBase):
    MaterialID: int

    class Config:
        from_attributes = True


# ── Aufgabe ────────────────────────────────────────────────────────────────────
class AufgabeBase(BaseModel):
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

class AufgabeCreate(AufgabeBase):
    pass

class AufgabeUpdate(AufgabeBase):
    pass

class AufgabeOut(AufgabeBase):
    AufgabeID: int

    class Config:
        from_attributes = True


# ── Datei ──────────────────────────────────────────────────────────────────────
class DateiBase(BaseModel):
    AufgabeID: int
    Dateipfad: str | None = None

class DateiCreate(DateiBase):
    pass

class DateiUpdate(DateiBase):
    pass

class DateiOut(DateiBase):
    DateiID: int

    class Config:
        from_attributes = True


# ── AufgabeMaterial ────────────────────────────────────────────────────────────
class AufgabeMaterialBase(BaseModel):
    AufgabeID: int
    MaterialID: int
    Anzahl: int | None = None

class AufgabeMaterialCreate(AufgabeMaterialBase):
    pass

class AufgabeMaterialUpdate(BaseModel):
    Anzahl: int | None = None

class AufgabeMaterialOut(AufgabeMaterialBase):
    class Config:
        from_attributes = True
