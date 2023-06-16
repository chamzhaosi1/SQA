import flask
from flask import request, jsonify
from calculator import Calculator

app = flask.Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    try:  
        data = request.get_json()
        # to make sure that the input is integer
        if isinstance(data['x'], int) and isinstance(data['y'], int):
            calculator = Calculator()
            result = calculator.add(data['x'], data['y'])
            return jsonify(result)
        else:
            raise ValueError("Input must be an integer.")
        
    except ValueError as e:  
        return jsonify({'error': str(e)})
    
@app.route('/sub', methods=['POST'])
def sub():  
    try: 
        data = request.get_json()
        # to make sure that the input is integer
        if isinstance(data['x'], int) and isinstance(data['y'], int):
            calculator = Calculator()
            result = calculator.sub(data['x'], data['y'])
            return jsonify(result)
        else:
            raise ValueError("Input must be an integer.")
        
    except Exception as e:  
        return jsonify({'error': str(e)})

@app.route('/div', methods=['POST'])
def div():
    try:
        data = request.get_json()
        # to make sure that the input is integer
        if isinstance(data['x'], int) and isinstance(data['y'], int):
            calculator = Calculator()
            result = calculator.div(data['x'], data['y'])
            return jsonify(result)
        else:
            raise ValueError("Input must be an integer.")
        
    except ValueError as e:  
        return jsonify({'error': str(e)})

@app.route('/mul', methods=['POST'])    
def mul():
    try:
        data = request.get_json()
        # to make sure that the input is integer
        if isinstance(data['x'], int) and isinstance(data['y'], int):
            calculator = Calculator()
            result = calculator.mul(data['x'], data['y']) 
            return jsonify(result)
        else:
            raise ValueError("Input must be an integer.")
        
    except Exception as e:  
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

# Run the app:
# python app.py
