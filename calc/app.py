from flask import Flask, request
import operations
app = Flask(__name__)


@app.route("/<operation>")
def operate(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    if operation == "add":
        return str(operations.add(a, b))
