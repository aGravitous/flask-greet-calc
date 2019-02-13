from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
    """Greets visitors."""

    html = f"""
    <html>
        <head></head>
        <body>
            <h1>Welcome</h1>
        </body>
    </html>
    """
    return html


@app.route('/welcome/<text>')
def welcome_page_with_text(text=""):
    """Greets visitors."""

    html = f"""
    <html>
        <head></head>
        <body>
            <h1>Welcome {text}</h1>
        </body>
    </html>
    """
    return html

# @app.route('/welcome/home')
# def welcome_page():
#     """Greets visitors."""

#     html = """
#     <html>
#         <head></head>
#         <body>
#             <h1>Welcome home</h1>
#         </body>
#     </html>
#     """
#     return html

# @app.route('/welcome/back')
# def welcome_page():
#     """Greets visitors."""

#     html = """
#     <html>
#         <head></head>
#         <body>
#             <h1>Welcome back</h1>
#         </body>
#     </html>
#     """
#     return html