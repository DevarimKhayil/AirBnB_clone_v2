# web_flask/1-hbnb_route.py

#!/usr/bin/python3
"""
A Flask web application that returns 'Hello HBNB!' on the root route
and 'HBNB' on the /hbnb route.
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

