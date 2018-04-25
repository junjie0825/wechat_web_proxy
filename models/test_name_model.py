import peewee
from models.base_model import BaseGameModel


# Define model
class TestNameModel(BaseGameModel):
    name = peewee.CharField()

    def __str__(self):
        return self.name
