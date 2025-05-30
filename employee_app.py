# App to manage company employee records using CRUD by Khairate Abdessamad

from db import get_connection

def add_employee(name, department, salary):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO employee (name, department, salary) VALUES (%s, %s, %s)"
    values = (name, department, salary)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print(f"Employee {name} added successfully.")

def list_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, department, salary FROM employee")
    for (emp_id, name, dept, sal) in cursor.fetchall():
        print(f"{emp_id}: {name} | {dept} | ${sal}")
    conn.close()

def update_employee(emp_id, name=None, department=None, salary=None):
    conn = get_connection()
    cursor = conn.cursor()
    updates = []
    values = []
    if name:
        updates.append("name=%s")
        values.append(name)
    if department:
        updates.append("department=%s")
        values.append(department)
    if salary:
        updates.append("salary=%s")
        values.append(salary)
    if not updates:
        print("No changes provided.")
        return
    sql = f"UPDATE employee SET {', '.join(updates)} WHERE id=%s"
    values.append(emp_id)
    cursor.execute(sql, tuple(values))
    conn.commit()
    conn.close()
    print(f"Employee {emp_id} updated successfully.")

def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee WHERE id=%s", (emp_id,))
    conn.commit()
    conn.close()
    print(f"Employee {emp_id} deleted successfully.")
