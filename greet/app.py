from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
    """Greets visitors."""

    html = """
    <html>
        <head></head>
        <body>
            <h1>Welcome!</h1>
        </body>
    </html>
    """
    return html