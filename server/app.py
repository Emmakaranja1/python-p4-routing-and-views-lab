#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


# Print string route
@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param


# Count route
@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param))
    return numbers + '\n'


# Math operation route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero'
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return 'Error: Modulo by zero'
        result = num1 % num2
    else:
        return 'Invalid operation'

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
