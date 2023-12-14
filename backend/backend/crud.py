from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == user_id).first()

def get_user_login(db: Session, email: str, password: str):
    fake_hashed_password = password + "notreallyhashed"
    return db.query(models.Usuario).filter(models.Usuario.email == email, models.Usuario.senha == fake_hashed_password).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UsuarioCreate):
    fake_hashed_password = user.senha + "notreallyhashed"
    db_user = models.Usuario(nome=user.nome, email=user.email, telefone=user.telefone, senha=fake_hashed_password, tipo=user.tipo)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_ponto_turistico(db: Session, ponto_turistico_id: int):
    return db.query(models.PontoTuristico).filter(models.PontoTuristico.id == ponto_turistico_id).first()

def get_pontos_turisticos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PontoTuristico).offset(skip).limit(limit).all()

def create_ponto_turistico(db: Session, ponto: schemas.PontoTuristico, user_id: int):
    db_item = models.PontoTuristico(**ponto.dict(), criador_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_foto_turismo(db: Session, foto_ponto_turistico_id: int):
    return db.query(models.FotosTurismo).filter(models.FotosTurismo.id == foto_ponto_turistico_id).first()

def get_fotos_turismo(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FotosTurismo).offset(skip).limit(limit).all()

def create_foto_turismo(db: Session, foto_turismo: schemas.FotosTurismo, ponto_id: int):
    db_item = models.FotosTurismo(**foto_turismo.dict(), ponto_fk=ponto_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_comentario(db: Session, comentario_id: int):
    return db.query(models.Comentario).filter(models.Comentario.id == comentario_id).first()

def get_comentarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comentario).offset(skip).limit(limit).all()

def create_comentario(db: Session, comentario: schemas.Comentario, user_id: int, ponto_id: int):
    db_item = models.Comentario(**comentario.dict(), usuario_id=user_id, ponto_turistico_id=ponto_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_foto_comentario(db: Session, foto_comentario_id: int):
    return db.query(models.FotosComentario).filter(models.FotosComentario.id == foto_comentario_id).first()

def get_fotos_comentario(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FotosComentario).offset(skip).limit(limit).all()

def create_foto_comentario(db: Session, foto_comentario: schemas.FotosComentario, comentario_id: int):
    db_item = models.FotosComentario(**foto_comentario.dict(), comentario_fk=comentario_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item