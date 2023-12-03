from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/usuarios/", response_model=schemas.Usuario)
def create_user(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado.")
    return crud.create_user(db=db, user=user)


@app.get("/usuarios/", response_model=list[schemas.Usuario])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/usuarios/{user_id}", response_model=schemas.Usuario)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return db_user


@app.post("/usuarios/{user_id}/pontos_turisticos/", response_model=schemas.PontoTuristico)
def create_item_for_user(
    user_id: int, ponto: schemas.PontoTuristicoCreate, db: Session = Depends(get_db)
):
    return crud.create_ponto_turistico(db=db, ponto=ponto, user_id=user_id)

@app.get("/pontos_turisticos/", response_model=list[schemas.PontoTuristico])
def read_pontos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pontos = crud.get_pontos_turisticos(db, skip=skip, limit=limit)
    return pontos

@app.get("/pontos_turisticos/{ponto_id}", response_model=schemas.PontoTuristico)
def read_pontos(ponto_id: int, db: Session = Depends(get_db)):
    ponto = crud.get_ponto_turistico(db, ponto_turistico_id=ponto_id)
    if ponto is None:
        raise HTTPException(status_code=404, detail="Ponto turístico não encontrado.")
    return ponto

@app.post("/usuarios/{user_id}/pontos_turisticos/{ponto_id}/comentarios/", response_model=schemas.Comentario)
def create_comentario_for_ponto(
    user_id: int, ponto_id: int, comentario: schemas.ComentarioCreate, db: Session = Depends(get_db)
):
    return crud.create_comentario(db=db, comentario=comentario, user_id=user_id, ponto_id=ponto_id)