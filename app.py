from flask import Flask, render_template, request, redirect
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

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method =='POST':
        title = request.form['title']
        description = request.form['desc']
        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
    allTodos = Todo.query.all()
    # print(allTodos)
    return render_template('index.html', allTodos=allTodos)

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route("/update/<int:sno>")
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


# debug mode, to get errors visible in brower 
if __name__ == "__main__":
    app.run(debug=True)


# SQLAlchemy: ORM mapper, helps to change Db using python