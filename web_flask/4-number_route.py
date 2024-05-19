# web_flask/4-number_route.py

#!/usr/bin/python3
"""
A Flask web application that returns:
- 'Hello HBNB!' on the root route
- 'HBNB' on the /hbnb route
- 'C ' followed by the value of the text variable on the /c/<text> route,
  with underscores replaced by spaces
- 'Python ' followed by the value of the text variable on the /python/<text> route,
  with underscores replaced by spaces, default value is 'is cool'
- 'n is a number' on the /number/<n> route, only if n is an integer
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that returns 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that returns 'HBNB'"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Route that returns 'C ' followed by the value of the text variable,
    with underscores replaced by spaces"""
    return "C " + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Route that returns 'Python ' followed by the value of the text variable,
    with underscores replaced by spaces. Default value is 'is cool'"""
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Route that returns 'n is a number' only if n is an integer"""
    return f"{n} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

