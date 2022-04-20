"""
There are 2 challenges. Only continue on to challenge 2 (bottom of file) if challenge 1 is completed.
Your boss is asking for a report of existing customers and their animals. Below is a small snippet of the database, in
order to, test the file before it is run against the production level database.
AC (acceptance criteria):
WHEN script is ran
THEN Customers are shown with their animals
example output (this is just to provide a visual of what is wanted):
    Grace is connected with Brixton
    Josh is connected with Micky
    Jeff is connected with Jack
    Jamal is connected with Snickers
    Megan is connected with Blue
    Caroline is connected with Scooby
"""

# CHALLENGE 1
ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Brixton",
        "species": "Dog",
        "customerId": 1
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "customerId": 5
    },
    {
        "id": 4,
        "name": "Micky",
        "species": "Mouse",
        "customerId": 2
    },
    {
        "id": 5,
        "name": "Scooby",
        "species": "Dog",
        "customerId": 6
    },
    {
        "id": 6,
        "name": "Jack",
        "species": "Rabbit",
        "customerId": 3
    }
]


CUSTOMERS = [
    {
        "id": 1,
        "name": "Grace",
        "age": 24
    },
    {
        "id": 2,
        "name": "Josh",
        "age": 18
    },
    {
        "id": 3,
        "name": "Jeff",
        "age": 37
    },
    {
        "id": 4,
        "name": "Jamal",
        "age": 41
    },
    {
        "id": 5,
        "name": "Megan",
        "age": 28
    },
    {
        "id": 6,
        "name": "Caroline",
        "age": 64
    }
]
# getting all animals and customers
def get_all_animals():
    return ANIMALS

def get_all_customers():
    return CUSTOMERS
# getting customers to match with the animal(by it's customerId)
# only nned to get by returned name since is running locally
def get_customers():
    for animal in ANIMALS:
        for customer in CUSTOMERS:
            if customer["id"] == animal["customerId"]:
                print(f"{customer['name']} is connected with {animal['name']}")
       
get_customers()