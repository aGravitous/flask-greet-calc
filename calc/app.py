from flask import Flask, request
import operations
app = Flask(__name__)

@app.route("/<operation>")
def operate(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    if operation == "add":
        return str(operations.add(a, b))
    elif operation == "sub":
        return str(operations.sub(a, b))
    elif operation == "mult":
        return str(operations.mult(a, b))
    elif operation == "div":
        return str(operations.div(a, b))


@app.route("/math/<operation>")
def operate_math(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    if operation == "add":
        return str(operations.add(a, b))
    elif operation == "sub":
        return str(operations.sub(a, b))
    elif operation == "mult":
        return str(operations.mult(a, b))
    elif operation == "div":
        return str(operations.div(a, b))
