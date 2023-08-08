from peewee import  CharField, FloatField, IntegerField, ForeignKeyField, AutoField
from modelos.Usuario import Usuario

from utils.ManagerDB import BaseModel

class Mascota(BaseModel):
    id_mascota = AutoField(primary_key=True)
    nombre = CharField(max_length=100)
    peso = FloatField()
    edad = IntegerField()
    raza = CharField(max_length=100)
    categoria = CharField(max_length=100)
    id_usuario_id= ForeignKeyField(Usuario, backref='mascotas', null=True)

