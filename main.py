from fastapi import FastAPI
from pizzas_logic.PizzaService import PizzaService

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
 
 
   