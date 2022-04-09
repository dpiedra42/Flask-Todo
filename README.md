# Flask-Todo

This is my flask web app that serves as a to-do list. To run it there are a few commands to do first.

1. Clone the repository wherever you'd like the app to be. 
2. Once cloned, you are going to create the virtual environment. This will have all the dependencies required by the project. You can do this by writing this command in the terminal:
    $ python3 -m venv venv
3. Next you are going to activate the virtual environment:
    $ . venv/bin/activate
4. Then, install all the dependencies:
    $ pip install -r requirements.txt
5.  Before you can run the project you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:
    $ export FLASK_APP=app
6. To enable all development features, set the FLASK_ENV environment variable to development.
    4 export FLASK_ENV=development
7. And finally you can run the app with:
    $ flask run

With my todo app you can add, remove, and check your tasks which will also remove it right away. When the app runs I start a database with SQLAlchemy that will hold all the tasks you add. The database will log an id, the task, the due date, and whether it is completed.

To add a task you need to both write the task and date by when you want to complete it When you click the add button the add function is triggered which will format the new todo task and commit it to the database. When you click remove, it triggers the delete function which will remove the task from the database by its id. 

Lastly, when you check the checkbox, the task checked will be hidden from the page but not removed from the database.

