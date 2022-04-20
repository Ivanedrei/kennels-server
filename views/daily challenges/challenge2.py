# CHALLENGE 2
# *** Make sure to comment out the above ANIMALS list and comment in the one below to use the updated data set ***
# *** You want to use the above CUSTOMERS list, still ***
# *** Make sure your code for challenge 1 is commented out to avoid conflicts ***
"""
You've realized that some customers may have multiple animals. 
AC (acceptance criteria):
WHEN script is ran
THEN Customers are shown with ALL their animals and the animal species
example output (this is just to provide a visual of what is wanted):
    Jamal is associated with the following animals -
     - Snickers (Dog)
    Grace is associated with the following animals -
     - Brixton (Dog)
     - Daisy (Cat)
    Megan is associated with the following animals -
     - Blue (Cat)
    Josh is associated with the following animals -
     - Micky (Mouse)
     - Minnie (Mouse)
     - Lucky (Rabbit)
    Caroline is associated with the following animals -
     - Scooby (Dog)
     - Goofy (Dog)
    Jeff is associated with the following animals -
     - Jack (Rabbit)
     - Winston (Dog)
     - Scruffy (Dog)
"""
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
    },
    {
        "id": 7,
        "name": "Winston",
        "species": "Dog",
        "customerId": 3
    },
    {
        "id": 8,
        "name": "Goofy",
        "species": "Dog",
        "customerId": 6
    },
    {
        "id": 8,
        "name": "Daisy",
        "species": "Cat",
        "customerId": 1
    },
    {
        "id": 10,
        "name": "Minnie",
        "species": "Mouse",
        "customerId": 2
    },
    {
        "id": 11,
        "name": "Scruffy",
        "species": "Dog",
        "customerId": 3
    },
    {
        "id": 12,
        "name": "Lucky",
        "species": "Rabbit",
        "customerId": 2
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
# function:
def get_customers():
    # loop over customers to display in order
    for customer in CUSTOMERS:
        # make the first sentence with each customer
        print(f"{customer['name']} is associated with the following animals -")
        # loop over animals to search for their customerId
        for animal in ANIMALS:
            if animal["customerId"] == customer["id"]:
                # we are displaying each animal by their customerId inside the customer(sentence loop).
                print(f"{animal['name']}")
                
get_customers()