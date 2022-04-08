from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create instance of class. First argument is the name of apps module/package
#__name__ is a varible set to Flask in this case
#needed so Flask knows where to look for sources
app = Flask(__name__)
#configuration to tell app how to connect to db, path to db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# will be removed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# binds db to app and provides access to all SQLAlchemy functions
db = SQLAlchemy(app)

# creating a Model: a python class which represents db table
class Todo(db.Model):
    # primary key creates unique id's
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    date = db.Column(db.String(100))
    completed = db.Column(db.Boolean)

# starts the database
db.create_all()

@app.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template('index.html', todo_list=todo_list)

# post method updates or creates 
@app.route('/add', methods=["POST"])
def add():
    task = request.form.get("Task")
    date = request.form.get("DueBy")
    new_todo = Todo(task=task, date=date, completed=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.completed
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
