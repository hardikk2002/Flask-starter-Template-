from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/products")
def products():
    return "<p>Hello, this is products!</p>"

# debug mode, to get errors visible in brower 
if __name__ == "__main__":
    app.run(debug=True)


# SQLAlchemy: ORM mapper, helps to change Db using python