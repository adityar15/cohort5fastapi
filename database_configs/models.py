from sqlalchemy import Column, Integer, String, Table, ForeignKey
from database_configs.connection import Base
from sqlalchemy.orm import relationship

pizzas_stats = Table('pizzas_stats', Base.metadata,
    Column('pizza_id', Integer, ForeignKey('pizzas.id')),
    Column('stat_id', Integer, ForeignKey('stats.id')))

pizzas_toppings = Table('pizzas_toppings', Base.metadata,
    Column('pizza_id', Integer, ForeignKey('pizzas.id')),
    Column('topping_id', Integer, ForeignKey('toppings.id')))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)

class Pizza(Base):
    __tablename__ = "pizzas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    basePrice = Column(Integer)
    toppings = relationship("Topping", secondary=pizzas_toppings, backref="pizzas") 
    stats = relationship("Stat", secondary=pizzas_stats, backref="pizzas"     )

class Topping(Base):
    __tablename__ = "toppings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    extraPrice = Column(Integer)
   

class Stat(Base):
    __tablename__ = "stats"
    id = Column(Integer, primary_key=True, index=True)
    stat_name = Column(String)
    stat_value = Column(String)
    extraPrice = Column(Integer)