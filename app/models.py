from . import db
from peewee import *


class Role(db.Model):
    id = PrimaryKeyField()
    name = CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'roles'


class User(db.Model):
    id = PrimaryKeyField()
    username = CharField(max_length=64, unique=True,
                                index=True)
    role = ForeignKeyField(Role, related_name='users', to_field='id', default=3)

    def __repr__(self):
        return '<User {0}>'.format(self.username)

    class Meta:
        db_table = 'users'
