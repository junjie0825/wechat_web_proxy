from sqlalchemy import Column, String, Integer, VARCHAR, ForeignKey, Float
from utils.database import Base


# Define model
class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer(), primary_key=True)
    name = Column(VARCHAR(20))
    age = Column(Integer())

    def __str__(self):
        return self.name
