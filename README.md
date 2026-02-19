# TaskFlow API

## Description
TaskFlow API is a RESTful backend service built with Django and Django REST Framework that allows users to securely manage personal tasks

## Features
- API Design
- Token-Based User Authentication
- Task CRUD operations
- Mark tasks as completed
- User specific task isolation

## Tech 
Python
Django
Django REST Framework

## API Endpoints
GET api/tasks/          List tasks
POST api/tasks/         Create tasks
GET api/tasks/<id>/     Retrieve task by id
PUT api/tasks/<id>/     Update task by id
DELETE api/tasks/<id>/  Delete task by id


## Installation / Setup

Follow the steps below to run the Task Manager API locally:

### 
1. Clone the repository

git clone https://github.com/solaajide/task-manager-api.git
cd taskmanager

2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Start the server
python manage.py runserver


You should see output like:
Starting development server at http://127.0.0.1:8000/


## Environment Variables

Create a file named .env in the root of the project and add:

SECRET_KEY=your-secret-key
DEBUG=True

Make sure .env is included in .gitignore so your secret key stays private.



## Author
Ajide Peculiar-Treasure

GitHub: https://github.com/solaajide