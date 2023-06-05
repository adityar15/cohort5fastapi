from fastapi import FastAPI, Depends
from pizzas_logic.PizzaService import PizzaService
from database_configs.connection import Base, engine, get_db
from database_configs import models
from sqlalchemy.orm import Session

from schemas.PizzaSchemas import PizzaCreateRequest

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Adi!"}

@app.get("/pizzas")
def getAllPizzas():
    pizzaService = PizzaService()
    return pizzaService.getAllPizzas()

@app.get("/pizzas/{pizza_name}")
def getPizzaByName(pizza_name : str):
    pizzaService = PizzaService()
    return pizzaService.getPizzaByName(pizza_name)
 

@app.post("/pizzas")
def createPizza(pizzaRequestBody: PizzaCreateRequest, db: Session = Depends(get_db)):
    # add it to the database
    pass
 
   