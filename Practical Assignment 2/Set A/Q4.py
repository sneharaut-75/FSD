from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Feedback Form</h2>
    <form method="POST" action="/feedback">
        Name: <input type="text" name="name"><br><br>
        Feedback: <textarea name="feedback"></textarea><br><br>
        <input type="submit" value="Submit Feedback">
    </form>
    '''

@app.route('/feedback', methods=['POST'])
def feedback():
    name = request.form['name']
    feedback = request.form['feedback']

    return f"Thank you {name}! Your feedback is: {feedback}"

if __name__ == '__main__':
    app.run(debug=True)