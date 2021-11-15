from sqlalchemy import Column, Integer, String, Date
from db import Base, engine

class Drivers(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    pass_number = Column(String(5))
    pass_series = Column(String(7))
    place_issue = Column(String(150))
    date_issue = Column(Date)
    date_arrive = Column(Date)
    

    def __repr__(self):
        return f'ID: {self.id}, name: {self.name}'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)