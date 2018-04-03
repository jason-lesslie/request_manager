# Feature Request Manager
The goal of this project was to build a feature request manager for new features a client desires to add to a piece of software. I used the following tech stack.
* Python 3.6
* MySQL Database
* flask
* SQLAlchemy
* Bootstrap
## Setup
* ensure you have `pip` and `virtualenv` and MySQL installed on your local machine
* setup virtual environment using following terminal command `virtualenv –p python3 venv`
* activate virtual environment `source venv/bin/activate`
* install all python requirements using `pip install –r requirements.txt`
* initialize MySQL database using `python manage.py db init`
* migrate MySQL database `python manage.py db migrate`
* update MySQL database to match models in python files `python manage.py db upgrade`
* start app with `python manage.py runserver`
* open browser and go to `http://localhost:5000/`
## Approach
I approached this project by first drawing up an entity relationship diagram of the database, normalizing the database, and laying out the database constraints. A PDF of my entity relationship diagram can be found in the main directory of this repository.
## Bugs/Challenges
* `unkown column 'request_model.client_request_priority'` This error is caused by database not having column for that model field. Resolved by using flask_migrate to perform a db migrate and upgrade. This gets adds/removes columns in the database to match model.
* client list priority drop down must manually set default value of client field to `1` ("Client A") without setting default value flask_wtf sets default value to string ``"None"``
* need to use python unittest module to add unit tests
##### Client Request Priority
* **Expected behavior:** client request priority field should dynamically adjust number of integers from (1 ... n)
* **Actual behavior:** request priority field is only showing the available priority integers for 'Client A'. Priority count id dynamic, but only works for default client.
* **Solution:** use KnockoutJS or AngularJS to apply two-way data binding. This would allow the client field to become a dependent field, which would allow the client priority drop down list to update on change to client field.
