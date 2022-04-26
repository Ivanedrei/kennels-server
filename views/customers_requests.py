import sqlite3
import json
from models import Customer

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
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
      SELECT 
        c.id,
        c.name,
        c.address,
        c.email
        FROM customer c
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row["name"], row['address'], row['email'])

            customers.append(customer.__dict__)

    return json.dumps(customers)

# Function with a single parameter
def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
          c.id,
          c.name,
          c.address,
          c.email
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        customer = Customer(data['id'], data["name"], data['address'], data['email'])

        return json.dumps(customer.__dict__)
  
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
