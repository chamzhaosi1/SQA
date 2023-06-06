import flask
from flask import request, jsonify
from calculator import Calculator

app = flask.Flask(__name__)

@app.route('/add', methods=['POST'])
def add():  
    data = request.get_json()
    calculator = Calculator()
    result = calculator.add(data['x'], data['y'])
    return jsonify(result)

@app.route('/sub', methods=['POST'])
def sub():  
    data = request.get_json()
    calculator = Calculator()
    result = calculator.sub(data['x'], data['y'])
    return jsonify(result)

@app.route('/div', methods=['POST'])
def div():
    data = request.get_json()
    calculator = Calculator()
    result = calculator.div(data['x'], data['y'])
    return jsonify(result)

@app.route('/mul', methods=['POST'])    
def mul():
    data = request.get_json()
    calculator = Calculator()
    result = calculator.mul(data['x'], data['y'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

# Run the app:
# python app.py
