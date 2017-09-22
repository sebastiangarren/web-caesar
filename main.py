from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border_radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form name="secret_maker" method="post">
            <input type="text" name="rot" value=0>
            <textarea name="text">{secret}</textarea>
            <input type="submit">
        </form>
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    secret_text = request.form["text"]
    rotation = request.form["rot"]
    rotation = int(rotation)
    encrypted = rotate_string(secret_text, rotation)
    return form.format(secret=encrypted)

@app.route("/")

def index():
    
    return form.format(secret=0)

app.run()