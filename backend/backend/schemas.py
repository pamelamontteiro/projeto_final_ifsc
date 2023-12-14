from pydantic import BaseModel
from datetime import date, datetime, time, timedelta

class FotosComentarioBase(BaseModel):
    foto_base: str

class FotosComentarioCreate(FotosComentarioBase):
    pass

class FotosComentario(FotosComentarioBase):
    id: int
    comentario_fk: int

    class Config:
        orm_mode = True

class ComentarioBase(BaseModel):
    texto: str
    nota: int

class ComentarioCreate(ComentarioBase):
    pass

class Comentario(ComentarioBase):
    id: int
    usuario_id: int
    ponto_turistico_id: int
    fotos_comentario: list[FotosComentario] = []

    class Config:
        orm_mode = True

class FotosTurismoBase(BaseModel):
    foto_url: str

class FotosTurismoCreate(FotosTurismoBase):
    pass

class FotosTurismo(FotosTurismoBase):
    id: int
    ponto_fk: int

    class Config:
        orm_mode = True


class PontoTuristicoBase(BaseModel):
    nome: str
    descricao: str
    bairro: str
    categoria: str
    nota: int

class PontoTuristicoCreate(PontoTuristicoBase):
    pass

class PontoTuristico(PontoTuristicoBase):
    id: int
    criador_id: int

    comentarios_ponto: list[Comentario] = []
    fotos_turismo: list[FotosTurismo] = []

    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    nome: str
    email: str
    tipo: int
    telefone: str


class UsuarioCreate(UsuarioBase):
    senha: str


class Usuario(UsuarioBase):
    id: int
    pontos: list[PontoTuristico] = []
    comentarios_usuario: list[Comentario] = []

    class Config:
        orm_mode = True
        
class UsuarioLogin(BaseModel):
    email: str
    senha: str