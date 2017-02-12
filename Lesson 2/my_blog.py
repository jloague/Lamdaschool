from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/birthday')
def birthday():
    return 'My birthday is July, 18 1982'


@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name + '!'


@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    return str(int(num1) + int(num2))


@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    return str(int(num1) * int(num2))


@app.route('/subtract/<num1>/<num2>')
def subtract(num1, num2):
    return str(int(num1) - int(num2))


@app.route('/favoritefoods')
def favoritefoods():
    myFood =['ramen', 'pizza', 'burgers', 'ribs', 'street tacos', 'fajitas']
    return jsonify(myFood)

if __name__ == "__main__":
    app.run()
