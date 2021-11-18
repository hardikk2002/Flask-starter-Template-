from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# to make schema ary has the follo
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # when we want to view the object then what it should show
    def __repr__(self) -> str:
        return f"{self.sno}- {self.title}"

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