from peewee import Model, PostgresqlDatabase

db = PostgresqlDatabase('AdopPetdb', user = "cesar",  password = 'root', host = 'localhost', port = 5432)

class BaseModel(Model):
    DB=db
    class Meta:
        database = db