from flask import Flask
import astley # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return astley.spamAstley()

if __name__ == "__main__":
    app.run(debug=True)
