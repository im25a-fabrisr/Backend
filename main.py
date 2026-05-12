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
    kategorie = db.query(models.Kategorie).filter(models.Kategorie.KategorieID == kategorie_id).first()
    if not kategorie:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden")
    return kategorie


@app.post("/kategorien/", response_model=schemas.KategorieOut, status_code=201)
def create_kategorie(kategorie: schemas.KategorieCreate, db: Session = Depends(get_db)):
    db_kategorie = models.Kategorie(**kategorie.model_dump())
    db.add(db_kategorie)
    db.commit()
    db.refresh(db_kategorie)
    return db_kategorie


@app.put("/kategorien/{kategorie_id}", response_model=schemas.KategorieOut)
def update_kategorie(kategorie_id: int, kategorie: schemas.KategorieUpdate, db: Session = Depends(get_db)):
    db_kategorie = db.query(models.Kategorie).filter(models.Kategorie.KategorieID == kategorie_id).first()
    if not db_kategorie:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden")
    for key, value in kategorie.model_dump().items():
        setattr(db_kategorie, key, value)
    db.commit()
    db.refresh(db_kategorie)
    return db_kategorie


@app.delete("/kategorien/{kategorie_id}", status_code=204)
def delete_kategorie(kategorie_id: int, db: Session = Depends(get_db)):
    db_kategorie = db.query(models.Kategorie).filter(models.Kategorie.KategorieID == kategorie_id).first()
    if not db_kategorie:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden")
    db.delete(db_kategorie)
    db.commit()
