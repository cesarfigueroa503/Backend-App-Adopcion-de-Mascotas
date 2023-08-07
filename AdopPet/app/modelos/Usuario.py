from peewee import  CharField, AutoField
from utils.ManagerDB import BaseModel




class Usuario(BaseModel):
    idusuario = AutoField(primary_key=True)
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    email = CharField(max_length=50, unique=True)
    contrasenia = CharField(max_length=100)



