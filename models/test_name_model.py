import peewee
from utils.databases import *


# Define model
class TestNameModel(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = database

    def __str__(self):
        return self.name
