from flask import Flask , request  ,render_template 
import psycopg2

app=Flask(__name__)

def get_connect():
    conn= psycopg2.connect(
        dbname= 'studentdb',
        user= 'postgres',
        password='root',
        host='localhost',
        port="5432"
    )
    return conn

def create_table():
    conn = get_connect()
    cur=conn.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Student(Student_ID SERIAL PRIMARY KEY, Name VARCHAR(100),Course VARCHAR(100))""")
    
    conn.commit()
    cur.close()
    conn.close()
    
@app.route('/student',methods=['GET','POST'])
def student():
    conn = get_connect()
    cur = conn.cursor()
    
    if request.method ==  'POST' :
        Name = request.form.get("name")
        Course  = request.form.get ("course")
        
        cur.execute("INSERT INTO Student(name ,course) VALUES(%s,%s)",(Name,Course) )
        conn.commit()
    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()    
        
    cur.close()
    conn.close()
        
    return render_template("index.html",students=students)
    
if __name__=='__main__':
    create_table()
    app.run(debug=True)