from fastapi import FastAPI, Depends, HTTPException
from pizzas_logic.PizzaService import PizzaService
from database_configs.connection import Base, engine, get_db
from database_configs import models
from sqlalchemy.orm import Session

from schemas.PizzaSchemas import PizzaCreateRequest, PizzaResponseModel
from schemas.ToppingSchemas import ToppingCreateRequest
from schemas.StatSchemas import StatCreateRequest

from origins import origins
from fastapi.middleware.cors import CORSMiddleware

from routes.attendance import router as attendanceRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(attendanceRouter)


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
 

# this tells FastAPI that the response body should be of type PizzaResponseModel
@app.post("/pizzas", response_model=PizzaResponseModel)
def createPizza(pizzaRequestBody: PizzaCreateRequest, db: Session = Depends(get_db)):
    # returns the number of toppings that are in the database from the array of toppings in the request body
    toppings = db.query(models.Topping).filter(models.Topping.id.in_(pizzaRequestBody.toppings)).all()

    # check if the toppings are valid
    # throws an HTTP error if the array are not the same length of the toppings in database
    if len(toppings) != len(pizzaRequestBody.toppings):
        raise HTTPException(status_code=422, detail="Toppings not found. You might want to create the toppings record first.")
        
    # can check for stats as well here. Maybe wannna do it as an exercise?


    # create the pizza in database
    pizza = models.Pizza(name=pizzaRequestBody.name, description=pizzaRequestBody.description, basePrice=pizzaRequestBody.basePrice)

    db.add(pizza)
   

    # add the toppings to the pizza
    pizza.toppings = toppings
    
    # commit the changes to the database
    # if you notice we are committing the pizza object at the end
    # not twice but once. This is because the toppings are added to the pizza object and we want to happen all in one transaction
    # if we commit the pizza first, use commit and then the associate, use commit again it will be two separate transactions and unnecessary commits. That's we set autocommmit to False in the connection.py file
    # so that we can control when to commit
    db.commit()


    return pizza
    
 
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



