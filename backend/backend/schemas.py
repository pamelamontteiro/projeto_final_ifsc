from pydantic import BaseModel

class ComentarioBase(BaseModel):
    texto: str
    nota: int

class ComentarioCreate(ComentarioBase):
    pass


class Comentario(ComentarioBase):
    id: int
    usuario_id: int
    ponto_turistico_id: int


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

    class Config:
        orm_mode = True


class UsuarioBase(BaseModel):
    nome: str
    email: str
    tipo: int


class UsuarioCreate(UsuarioBase):
    senha: str


class Usuario(UsuarioBase):
    id: int
    pontos: list[PontoTuristico] = []
    comentarios_usuario: list[Comentario] = []

    class Config:
        orm_mode = True
