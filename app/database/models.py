from app import db
from peewee import *


class BaseModel(Model):

    class Meta:
        database = db

class Role(BaseModel):
    id = PrimaryKeyField()
    name = CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'roles'


class User(BaseModel):
    id = PrimaryKeyField()
    username = CharField(max_length=64, unique=True,
                                index=True)
    role = ForeignKeyField(Role, related_name='users', to_field='id', default=3)

    def __repr__(self):
        return '<User {0}>'.format(self.username)

    class Meta:
        db_table = 'users'

class Assessment(BaseModel):
    id = PrimaryKeyField()
    doc_id = IntegerField(index=True)
    square_id = IntegerField()
    square_text = TextField()
    label_0 = IntegerField(null=True)
    label_1 = IntegerField(null=True)
    label_2 = IntegerField(null=True)
    label_3 = IntegerField(null=True)
    label_4 = IntegerField(null=True)
    label_5 = IntegerField(null=True)
    rated = BooleanField(default=False)


MODELS_LIST = [User, Assessment]