from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    welcome = float(request.form['welcome'])
    percent = int(request.form['percent'])
    remain = welcome - (welcome * percent / 100)
    people = int(request.form['people'])
    total_per_person = remain / people
    return render_template('result.html', total_per_person=total_per_person)

if __name__ == '__main__':
    app.run(debug=True)
