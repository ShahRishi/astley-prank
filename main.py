from flask import Flask
import astley 

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return astley.spamAstley()

if __name__ == "__main__":
    app.run(debug=True)
