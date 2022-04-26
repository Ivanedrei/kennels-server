import sqlite3
import json
from models import Employee


EMPLOYEES = [
        {
      "id": 1,
      "name": "jack",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "jake",
      "locationId": 2
    },
    {
      "id": 4,
      "name": "melissa",
      "locationId": 1
    },
    {
      "id": 5,
      "name": "sarah",
      "locationId": 2
    }
  ]

def get_all_employees():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
       SELECT
          e.id,
          e.name,
          e.location_Id
      FROM customer e
      """, (id, ))

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row["id"], row["name"], row["location_id"])
            employees.append(employee.__dict__)

        return json.dumps(employees)
# Function with a single parameter
def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
          e.id,
          e.name,
          e.location_Id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        employee = Employee(data["id"], data["name"], data["location_id"])

        return json.dumps(employee.__dict__)

def create_employee(employee):
    max_id = EMPLOYEES[-1] ["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break