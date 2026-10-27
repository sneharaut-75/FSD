from flask import Flask
import psycopg2

app = Flask(__name__)

def dbconnect():
    return psycopg2.connect(
        dbname='emp',
        user='postgres',
        password='root',
        host='localhost',
        port=5432
    )

@app.route('/createtable')
def createtable():
    conn = dbconnect()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS emp (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100),
            salary INT
        );
    ''')

    conn.commit()
    cur.close()
    conn.close()

    return "table created successfully"


@app.route('/insertrec')
def insertrec():
    employees = [
        ('Sneha', 'IT', 1000),
        ('Trupti', 'Transport', 11000),
        ('Gayatri', 'Finance', 52000),
        ('Kiran', 'Back Office', 18000),
        ('Pranita', 'Sales', 17000)
    ]

    conn = dbconnect()
    cur = conn.cursor()

    cur.executemany('''
        INSERT INTO emp(name, department, salary)
        VALUES (%s, %s, %s);
    ''', employees)

    conn.commit()
    cur.close()
    conn.close()

    return "records inserted successfully"


@app.route('/getdetails/<int:id>')
def getdetails(id):
    conn = dbconnect()
    cur = conn.cursor()

    cur.execute('''
        SELECT id, name, department, salary
        FROM emp
        WHERE id = %s;
    ''', (id,))

    emp = cur.fetchone()

    cur.close()
    conn.close()

    if emp:
        return f"""
            ID: {emp[0]}<br>
            Name: {emp[1]}<br>
            Department: {emp[2]}<br>
            Salary: {emp[3]}
        """

    return "Employee not found"


app.run(debug=True)

