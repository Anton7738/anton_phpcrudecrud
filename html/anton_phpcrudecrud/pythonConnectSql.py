import sqlite3

connection = sqlite3.connect('employees')

def execute_query(query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


