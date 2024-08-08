import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    contraseña = Column(String(250), nullable=False)
    fecha_subscripcion = Column(DateTime, default=datetime.utcnow)

    planetas_favoritos = relationship('Favorito', foreign_keys='Favorito.usuario_id', back_populates='usuario')
    personajes_favoritos = relationship('Favorito', foreign_keys='Favorito.usuario_id', back_populates='usuario')


class Planeta(Base):
    __tablename__ = 'planeta'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    clima = Column(String(250))
    terreno = Column(String(250))

    
    favoritos = relationship('Favorito', foreign_keys='Favorito.planeta_id', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personaje'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    altura = Column(Integer)
    peso = Column(Integer)
    color_cabello = Column(String(250))
    color_piel = Column(String(250))
    color_ojo = Column(String(250))


    favoritos = relationship('Favorito', foreign_keys='Favorito.personaje_id', back_populates='personaje')

class Favorito(Base):
    __tablename__ = 'favorito'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)

    usuario = relationship('Usuario', back_populates='planetas_favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')

render_er(Base, 'diagram.png')

