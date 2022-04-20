CUSTOMERS = [
    {
      "id": 1,
      "name": "Sydney Noh",
      "address": "976 Software School Rd.",
      "email": "sydneyN@nss.com"
    },
    {
      "id": 2,
      "name": "Trevor Guinn",
      "address": "123 NSS Ln",
      "email": "trevorG@nss.com"
    },
    {
      "id": 3,
      "name": "Ivan Ramirez",
      "address": "572 Main St.",
      "email": "ivanR@nss.com"
    },
    {
      "id": 4,
      "name": "Bob Marley",
      "address": "321 NotYour St.",
      "email": "bobM@nss.com"
    },
    {
      "id": 5,
      "name": "Michael Jordan",
      "address": "123 NotUr St.",
      "email": "michaelJ@nss.com"
    },
    {
      "email": "me@me.com",
      "name": "Ivan Vera",
      "id": 6
    }
]

def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
  
def create_customer(customer):
    max_id = CUSTOMERS[-1] ["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
      if customer["id"] == id:
          CUSTOMERS[index] = new_customer
          break
