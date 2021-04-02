# importing flask for server functionality in app.py
from flask import Flask
app = Flask(__name__)

# importing ability to handle requests from flask
from flask import request

# importing all functions from operations.py file
from operations import add, sub, mult, div

@app.route('/add')
def _add(a, b):
    """Calls add() function from operations and returns the result."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    addition = add(a, b)
    html = f"<html><body><h1>{a} + {b} is...</h1><h3>{addition}</h3></body></html"
    return html

@app.route('/sub')
def _subtract(a, b):
    """Calls sub() function from operations and returns the result."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    subtraction = sub(a, b)
    html = f"<html><body><h1>{a} - {b} is...</h1><h3>{subtraction}</h3></body></html"
    return html

@app.route('/mult')
def _muliplyt(a, b):
    """Calls mult() function from operations and returns the result."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    multiplication = mult(a, b)
    html = f"<html><body><h1>{a} * {b} is...</h1><h3>{multiplication}</h3></body></html"
    return html

@app.route('/div')
def _division(a, b):
    """Calls div() function from operations and returns the result."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    division = div(a, b)
    html = f"<html><body><h1>{a} / {b} is...</h1><h3>{division}</h3></body></html"
    return str(division)


# PART II

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<opera>")
def do_math(opera):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[opera](a, b)

    return str(result)