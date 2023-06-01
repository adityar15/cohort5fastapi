class PizzaService: 
    def __init__(self):
        self.pizzaRecords = [
    {
        "id": 1,
        "name": "pepporoni pizza",
        "description": "Pizza with Pepporoni",
        "basePrice": 12,
        "stats": [
            {
                "id": 1,
                "size": "Small",
                "extraPrice": 0
            },
             {
                "id": 2,
                "size": "Medium",
                "extraPrice": 1
            },
              {
                "id": 3,
                "size": "Large",
                "extraPrice": 2
            },
        ]
    },
      {
        "id": 2,
        "name": "chicken pizza",
        "description": "Pizza with Chicken",
        "basePrice": 12,
        "stats": [
            {
                "id": 1,
                "size": "Small",
                "extraPrice": 0
            },
             {
                "id": 2,
                "size": "Medium",
                "extraPrice": 1
            },
              {
                "id": 3,
                "size": "Large",
                "extraPrice": 2
            },
        ]
    }
    ]

    def getAllPizzas(self):
        return self.pizzaRecords
    
    def getPizzaByName(self, pizza_name : str):
    
        for pizza in self.pizzaRecords:

            if pizza["name"].__contains__(pizza_name.lower()):
                return pizza
            
        return {"message": "Pizza not found!"}