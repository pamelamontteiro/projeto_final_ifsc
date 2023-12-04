from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    tipo = Column(Integer)

    pontos = relationship("PontoTuristico", back_populates="criador")
    comentarios_usuario = relationship("Comentario", back_populates="usuario")



class PontoTuristico(Base):
    __tablename__ = "ponto_turistico"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String, index=True)
    bairro = Column(String, index=True)
    categoria = Column(String, index=True)
    nota = Column(Integer, index=True)
    
    criador_id = Column(Integer, ForeignKey("usuario.id"))
    
    criador = relationship("Usuario", back_populates="pontos")
    comentarios_ponto = relationship("Comentario", back_populates="ponto_turistico")


class Comentario(Base):
    __tablename__ = "comentario"

    id = Column(Integer, primary_key=True, index=True)
    texto = Column(String, index=True)
    nota = Column(Integer, index=True)

    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    ponto_turistico_id = Column(Integer, ForeignKey("ponto_turistico.id"))

    usuario = relationship("Usuario", back_populates="comentarios_usuario")
    ponto_turistico = relationship("PontoTuristico", back_populates="comentarios_ponto")