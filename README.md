# Task Management

It is a Task Management System project which allow the users to to create, read, update, and delete tasks. The RESTful APIs for backend is created using Python/Django and for database it uses Postgresql. Django Rest Framework is used to develop the APIs.

Setup
The first thing to do is to clone the repository:

$ git clone https://github.com/amitgautam1994/TaskManagement.git
Create a virtual environment to install dependencies in and activate it:

$ virtualenv venv
For Windows:
$ venv/Script/activate

Then install the dependencies:

(venv)$ pip install -r requirements.txt
Note the (venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

(venv)$ cd TaskManagement

We need to setup the postgres Db and add the credentials in ".env" file.

(venv)$ python manage.py runserver

First we need to register
For register Navigate to http://127.0.0.1:8000/api/register/
Enter details and submit.

Then we need to login and get access key
For register Navigate to http://127.0.0.1:8000/api/login/
Enter username and password and submit. We will get access token, which we have to use in Header while testing the Task related API

Create task
We can create task by navigating http://127.0.0.1:8000/api/create/
We also need to add access token in Header
e.g. Authorization : Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1MzAzMzMwLCJpYXQiOjE2OTUzMDMwM

Get task by ID
We can get a task using ID by navigating http://127.0.0.1:8000/api/task_detail/id
e.g. http://127.0.0.1:8000/api/task_detail/2
We also need to add access token in Header
e.g. Authorization : Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1MzAzMzMwLCJpYXQiOjE2OTUzMDMwM

Get all tasks
We can get list of all the tasks by navigating http://127.0.0.1:8000/api/tasks/
We also need to add access token in Header
e.g. Authorization : Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1MzAzMzMwLCJpYXQiOjE2OTUzMDMwM

Update task by ID
We can update a task using ID by navigating http://127.0.0.1:8000/api/update/id
e.g. http://127.0.0.1:8000/api/update/2
We also need to add access token in Header
e.g. Authorization : Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1MzAzMzMwLCJpYXQiOjE2OTUzMDMwM

Delete task by ID
We can delete a task using ID by navigating http://127.0.0.1:8000/api/delete/id
e.g. http://127.0.0.1:8000/api/delete/2
We also need to add access token in Header
e.g. Authorization : Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1MzAzMzMwLCJpYXQiOjE2OTUzMDMwM
