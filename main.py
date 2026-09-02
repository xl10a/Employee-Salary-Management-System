import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'jard.db')

conn = sqlite3.connect(db_path)
conn.execute('CREATE TABLE IF NOT EXISTS employees (name TEXT, salary REAL)')

while True:
    print("\n--- Salary Management System ---")
    print("1. Add new employee")
    print("2. Show all employees")
    print("3. Exit")

    choice = input("Choose a number: ")

    if choice == '1':
        name = input("Employee name: ")
        salary = float(input("Salary: "))
        conn.execute("INSERT INTO employees VALUES (?,?)", (name, salary))
        conn.commit()
        print(f"Saved {name} to the system!")

    elif choice == '2':
        print("\n--- Employee List ---")
        for row in conn.execute("SELECT * FROM employees"):
            print(f"Name: {row[0]} - Salary: {row[1]}")

    elif choice == '3':
        break

conn.close()
print("System closed. Goodbye!")
