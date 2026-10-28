from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Connect to database
def db_connect():
    return psycopg2.connect(
        dbname="jobportal",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )


# Create Job and Application tables
def create_tables():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Job (
            Job_ID SERIAL PRIMARY KEY,
            Title VARCHAR(100),
            Company VARCHAR(100),
            Location VARCHAR(100),
            Salary FLOAT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Application (
            Application_ID SERIAL PRIMARY KEY,
            Applicant_Name VARCHAR(100),
            Email VARCHAR(100),
            Job_ID INT REFERENCES Job(Job_ID) ON DELETE CASCADE
        )
    """)

    con.commit()
    cur.close()
    con.close()


# Add job
@app.route("/", methods=["GET", "POST"])
def add_job():
    if request.method == "POST":
        title = request.form["Title"]
        company = request.form["Company"]
        location = request.form["Location"]
        salary = request.form["Salary"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO Job (Title, Company, Location, Salary) VALUES (%s, %s, %s, %s)",
            (title, company, location, salary)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/job")

    return render_template("add.html")


# Display jobs
@app.route("/job")
def display_jobs():
    con = db_connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM Job ORDER BY Job_ID")
    jobs = cur.fetchall()

    cur.close()
    con.close()

    return render_template("job.html", jobs=jobs)


# Search jobs by title or location
@app.route("/search", methods=["GET", "POST"])
def search_job():
    jobs = None
    keyword = ""

    if request.method == "POST":
        keyword = request.form["Keyword"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM Job WHERE Title ILIKE %s OR Location ILIKE %s ORDER BY Job_ID",
            ("%" + keyword + "%", "%" + keyword + "%")
        )
        jobs = cur.fetchall()

        cur.close()
        con.close()

    return render_template("search.html", jobs=jobs, keyword=keyword)


# Apply for a job
@app.route("/apply", methods=["GET", "POST"])
def apply_job():
    con = db_connect()
    cur = con.cursor()

    if request.method == "POST":
        name = request.form["Applicant_Name"]
        email = request.form["Email"]
        job_id = request.form["Job_ID"]

        cur.execute(
            "INSERT INTO Application (Applicant_Name, Email, Job_ID) VALUES (%s, %s, %s)",
            (name, email, job_id)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/applications")

    cur.execute("SELECT Job_ID, Title, Company FROM Job ORDER BY Job_ID")
    jobs = cur.fetchall()

    cur.close()
    con.close()

    return render_template("apply.html", jobs=jobs)


# Display applications
@app.route("/applications")
def display_applications():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        SELECT a.Application_ID, a.Applicant_Name, a.Email, j.Title, j.Company
        FROM Application a
        JOIN Job j ON a.Job_ID = j.Job_ID
        ORDER BY a.Application_ID
    """)
    applications = cur.fetchall()

    cur.close()
    con.close()

    return render_template("applications.html", applications=applications)

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
