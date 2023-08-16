from peewee import Model, PostgresqlDatabase

db = PostgresqlDatabase('proyecto', user = "grupo1" , password= "123", host = '192.168.1.30', port = 5432)

class BaseModel(Model):
    DB=db
    class Meta:
        database = db
