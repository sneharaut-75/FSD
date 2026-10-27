from flask import Flask
import platform

app = Flask(__name__)

@app.route('/')
def home():
    return "System Information Application"

@app.route('/system')
def system():
    return f"""
    Operating System: {platform.system()} <br>
    Release: {platform.release()} <br>
    Processor: {platform.processor()}
    """

if __name__ == '__main__':
    app.run(debug=True)