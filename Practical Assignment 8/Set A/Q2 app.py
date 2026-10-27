from flask import Flask
import psycopg2
app = Flask(__name__)
@app.route('/')
def home():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            marks INT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    return "Student Table Created Successfully"
if __name__ == '__main__':
    app.run(debug=True)
