from pydantic import BaseModel
from datetime import datetime

class AufgabeCreate(BaseModel):
    titel: str
    beginn: datetime | None = None
    ende: datetime | None = None
    ort: str | None = None
    koordinaten: str | None = None
    notiz: str | None = None
    kategorie_id: int | None = None
    prioritaet_id: int | None = None
    fortschritt_id: int | None = None
    benutzer_id: int