from flask import Flask
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def show_datetime():
    now = datetime.now()
    return f"Current Date and Time: {now}"
app.run(debug=True)