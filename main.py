from fastapi import FastAPI, Depends
from pizzas_logic.PizzaService import PizzaService
from database_configs.connection import Base, engine, get_db
from database_configs import models
from sqlalchemy.orm import Session

from schemas.PizzaSchemas import PizzaCreateRequest
from schemas.ToppingSchemas import ToppingCreateRequest
from schemas.StatSchemas import StatCreateRequest

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
    toppings = db.query(models.Topping).filter(models.Topping.id.in_(pizzaRequestBody.toppings)).all()
    pass
 
@app.post("/toppings")
def createToppings(toppingRequest: ToppingCreateRequest, db: Session = Depends(get_db)):
   topping = models.Topping(name= toppingRequest.name, description=toppingRequest.description, extraPrice=toppingRequest.extraPrice)

   db.add(topping)
   db.commit()
   db.refresh(topping)

   return topping



@app.get("/toppings")
def getAllToppings(db: Session = Depends(get_db)):
    return db.query(models.Topping).all()
# select * from toppings


@app.post("/stats")
def createStats(statRequest: StatCreateRequest, db: Session = Depends(get_db)):
   stat = models.Stat(stat_name= statRequest.stat_name, stat_value=statRequest.stat_value, extraPrice=statRequest.extraPrice)

   db.add(stat)
   db.commit()
   db.refresh(stat)

   return stat



@app.get("/stats")
def getAllStats(db: Session = Depends(get_db)):
    return db.query(models.Stat).all()



