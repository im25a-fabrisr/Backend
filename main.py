from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# ── Kategorie ──────────────────────────────────────────────────────────────────

@app.get("/kategorien/", response_model=list[schemas.KategorieOut])
def get_kategorien(db: Session = Depends(get_db)):
    return db.query(models.Kategorie).all()


@app.get("/kategorien/{kategorie_id}", response_model=schemas.KategorieOut)
def get_kategorie(kategorie_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Kategorie).filter(models.Kategorie.KategorieID == kategorie_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden")
    return eintrag


@app.post("/kategorien/", response_model=schemas.KategorieOut, status_code=201)
def create_kategorie(daten: schemas.KategorieCreate, db: Session = Depends(get_db)):
    eintrag = models.Kategorie(**daten.model_dump())
    db.add(eintrag)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.put("/kategorien/{kategorie_id}", response_model=schemas.KategorieOut)
def update_kategorie(kategorie_id: int, daten: schemas.KategorieUpdate, db: Session = Depends(get_db)):
    eintrag = db.query(models.Kategorie).filter(models.Kategorie.KategorieID == kategorie_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden")
    for key, value in daten.model_dump().items():
        setattr(eintrag, key, value)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.delete("/kategorien/{kategorie_id}", status_code=204)
def delete_kategorie(kategorie_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Kategorie).filter(models.Kategorie.KategorieID == kategorie_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden")
    db.delete(eintrag)
    db.commit()


# ── Prioritaet ─────────────────────────────────────────────────────────────────

@app.get("/prioritaeten/", response_model=list[schemas.PrioritaetOut])
def get_prioritaeten(db: Session = Depends(get_db)):
    return db.query(models.Prioritaet).all()


@app.get("/prioritaeten/{prioritaet_id}", response_model=schemas.PrioritaetOut)
def get_prioritaet(prioritaet_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Prioritaet).filter(models.Prioritaet.PrioritaetID == prioritaet_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Prioritaet nicht gefunden")
    return eintrag


@app.post("/prioritaeten/", response_model=schemas.PrioritaetOut, status_code=201)
def create_prioritaet(daten: schemas.PrioritaetCreate, db: Session = Depends(get_db)):
    eintrag = models.Prioritaet(**daten.model_dump())
    db.add(eintrag)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.put("/prioritaeten/{prioritaet_id}", response_model=schemas.PrioritaetOut)
def update_prioritaet(prioritaet_id: int, daten: schemas.PrioritaetUpdate, db: Session = Depends(get_db)):
    eintrag = db.query(models.Prioritaet).filter(models.Prioritaet.PrioritaetID == prioritaet_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Prioritaet nicht gefunden")
    for key, value in daten.model_dump().items():
        setattr(eintrag, key, value)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.delete("/prioritaeten/{prioritaet_id}", status_code=204)
def delete_prioritaet(prioritaet_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Prioritaet).filter(models.Prioritaet.PrioritaetID == prioritaet_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Prioritaet nicht gefunden")
    db.delete(eintrag)
    db.commit()


# ── Fortschritt ────────────────────────────────────────────────────────────────

@app.get("/fortschritte/", response_model=list[schemas.FortschrittOut])
def get_fortschritte(db: Session = Depends(get_db)):
    return db.query(models.Fortschritt).all()


@app.get("/fortschritte/{fortschritt_id}", response_model=schemas.FortschrittOut)
def get_fortschritt(fortschritt_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Fortschritt).filter(models.Fortschritt.FortschrittID == fortschritt_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Fortschritt nicht gefunden")
    return eintrag


@app.post("/fortschritte/", response_model=schemas.FortschrittOut, status_code=201)
def create_fortschritt(daten: schemas.FortschrittCreate, db: Session = Depends(get_db)):
    eintrag = models.Fortschritt(**daten.model_dump())
    db.add(eintrag)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.put("/fortschritte/{fortschritt_id}", response_model=schemas.FortschrittOut)
def update_fortschritt(fortschritt_id: int, daten: schemas.FortschrittUpdate, db: Session = Depends(get_db)):
    eintrag = db.query(models.Fortschritt).filter(models.Fortschritt.FortschrittID == fortschritt_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Fortschritt nicht gefunden")
    for key, value in daten.model_dump().items():
        setattr(eintrag, key, value)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.delete("/fortschritte/{fortschritt_id}", status_code=204)
def delete_fortschritt(fortschritt_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Fortschritt).filter(models.Fortschritt.FortschrittID == fortschritt_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Fortschritt nicht gefunden")
    db.delete(eintrag)
    db.commit()


# ── Benutzer ───────────────────────────────────────────────────────────────────

@app.get("/benutzer/", response_model=list[schemas.BenutzerOut])
def get_benutzer_alle(db: Session = Depends(get_db)):
    return db.query(models.Benutzer).all()


@app.get("/benutzer/{benutzer_id}", response_model=schemas.BenutzerOut)
def get_benutzer(benutzer_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Benutzer).filter(models.Benutzer.BenutzerID == benutzer_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    return eintrag


@app.post("/benutzer/", response_model=schemas.BenutzerOut, status_code=201)
def create_benutzer(daten: schemas.BenutzerCreate, db: Session = Depends(get_db)):
    eintrag = models.Benutzer(**daten.model_dump())
    db.add(eintrag)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.put("/benutzer/{benutzer_id}", response_model=schemas.BenutzerOut)
def update_benutzer(benutzer_id: int, daten: schemas.BenutzerUpdate, db: Session = Depends(get_db)):
    eintrag = db.query(models.Benutzer).filter(models.Benutzer.BenutzerID == benutzer_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    for key, value in daten.model_dump().items():
        setattr(eintrag, key, value)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.delete("/benutzer/{benutzer_id}", status_code=204)
def delete_benutzer(benutzer_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Benutzer).filter(models.Benutzer.BenutzerID == benutzer_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    db.delete(eintrag)
    db.commit()


# ── Material ───────────────────────────────────────────────────────────────────

@app.get("/materialien/", response_model=list[schemas.MaterialOut])
def get_materialien(db: Session = Depends(get_db)):
    return db.query(models.Material).all()


@app.get("/materialien/{material_id}", response_model=schemas.MaterialOut)
def get_material(material_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Material).filter(models.Material.MaterialID == material_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")
    return eintrag


@app.post("/materialien/", response_model=schemas.MaterialOut, status_code=201)
def create_material(daten: schemas.MaterialCreate, db: Session = Depends(get_db)):
    eintrag = models.Material(**daten.model_dump())
    db.add(eintrag)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.put("/materialien/{material_id}", response_model=schemas.MaterialOut)
def update_material(material_id: int, daten: schemas.MaterialUpdate, db: Session = Depends(get_db)):
    eintrag = db.query(models.Material).filter(models.Material.MaterialID == material_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")
    for key, value in daten.model_dump().items():
        setattr(eintrag, key, value)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.delete("/materialien/{material_id}", status_code=204)
def delete_material(material_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Material).filter(models.Material.MaterialID == material_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")
    db.delete(eintrag)
    db.commit()


# ── Aufgabe ────────────────────────────────────────────────────────────────────

@app.get("/aufgaben/", response_model=list[schemas.AufgabeOut])
def get_aufgaben(db: Session = Depends(get_db)):
    return db.query(models.Aufgabe).all()


@app.get("/aufgaben/{aufgabe_id}", response_model=schemas.AufgabeOut)
def get_aufgabe(aufgabe_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Aufgabe).filter(models.Aufgabe.AufgabeID == aufgabe_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    return eintrag


@app.post("/aufgaben/", response_model=schemas.AufgabeOut, status_code=201)
def create_aufgabe(daten: schemas.AufgabeCreate, db: Session = Depends(get_db)):
    eintrag = models.Aufgabe(**daten.model_dump())
    db.add(eintrag)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.put("/aufgaben/{aufgabe_id}", response_model=schemas.AufgabeOut)
def update_aufgabe(aufgabe_id: int, daten: schemas.AufgabeUpdate, db: Session = Depends(get_db)):
    eintrag = db.query(models.Aufgabe).filter(models.Aufgabe.AufgabeID == aufgabe_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    for key, value in daten.model_dump().items():
        setattr(eintrag, key, value)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.delete("/aufgaben/{aufgabe_id}", status_code=204)
def delete_aufgabe(aufgabe_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Aufgabe).filter(models.Aufgabe.AufgabeID == aufgabe_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Aufgabe nicht gefunden")
    db.delete(eintrag)
    db.commit()


# ── Datei ──────────────────────────────────────────────────────────────────────

@app.get("/dateien/", response_model=list[schemas.DateiOut])
def get_dateien(db: Session = Depends(get_db)):
    return db.query(models.Datei).all()


@app.get("/dateien/{datei_id}", response_model=schemas.DateiOut)
def get_datei(datei_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Datei).filter(models.Datei.DateiID == datei_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Datei nicht gefunden")
    return eintrag


@app.post("/dateien/", response_model=schemas.DateiOut, status_code=201)
def create_datei(daten: schemas.DateiCreate, db: Session = Depends(get_db)):
    eintrag = models.Datei(**daten.model_dump())
    db.add(eintrag)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.put("/dateien/{datei_id}", response_model=schemas.DateiOut)
def update_datei(datei_id: int, daten: schemas.DateiUpdate, db: Session = Depends(get_db)):
    eintrag = db.query(models.Datei).filter(models.Datei.DateiID == datei_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Datei nicht gefunden")
    for key, value in daten.model_dump().items():
        setattr(eintrag, key, value)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.delete("/dateien/{datei_id}", status_code=204)
def delete_datei(datei_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.Datei).filter(models.Datei.DateiID == datei_id).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="Datei nicht gefunden")
    db.delete(eintrag)
    db.commit()


# ── AufgabeMaterial ────────────────────────────────────────────────────────────

@app.get("/aufgabe-material/", response_model=list[schemas.AufgabeMaterialOut])
def get_aufgabe_material_alle(db: Session = Depends(get_db)):
    return db.query(models.AufgabeMaterial).all()


@app.get("/aufgabe-material/{aufgabe_id}/{material_id}", response_model=schemas.AufgabeMaterialOut)
def get_aufgabe_material(aufgabe_id: int, material_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.AufgabeMaterial).filter(
        models.AufgabeMaterial.AufgabeID == aufgabe_id,
        models.AufgabeMaterial.MaterialID == material_id
    ).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="AufgabeMaterial nicht gefunden")
    return eintrag


@app.post("/aufgabe-material/", response_model=schemas.AufgabeMaterialOut, status_code=201)
def create_aufgabe_material(daten: schemas.AufgabeMaterialCreate, db: Session = Depends(get_db)):
    eintrag = models.AufgabeMaterial(**daten.model_dump())
    db.add(eintrag)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.put("/aufgabe-material/{aufgabe_id}/{material_id}", response_model=schemas.AufgabeMaterialOut)
def update_aufgabe_material(aufgabe_id: int, material_id: int, daten: schemas.AufgabeMaterialUpdate, db: Session = Depends(get_db)):
    eintrag = db.query(models.AufgabeMaterial).filter(
        models.AufgabeMaterial.AufgabeID == aufgabe_id,
        models.AufgabeMaterial.MaterialID == material_id
    ).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="AufgabeMaterial nicht gefunden")
    for key, value in daten.model_dump().items():
        setattr(eintrag, key, value)
    db.commit()
    db.refresh(eintrag)
    return eintrag


@app.delete("/aufgabe-material/{aufgabe_id}/{material_id}", status_code=204)
def delete_aufgabe_material(aufgabe_id: int, material_id: int, db: Session = Depends(get_db)):
    eintrag = db.query(models.AufgabeMaterial).filter(
        models.AufgabeMaterial.AufgabeID == aufgabe_id,
        models.AufgabeMaterial.MaterialID == material_id
    ).first()
    if not eintrag:
        raise HTTPException(status_code=404, detail="AufgabeMaterial nicht gefunden")
    db.delete(eintrag)
    db.commit()
