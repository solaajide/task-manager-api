# TaskFlow API

## Description
TaskFlow API is a RESTful backend service built with Django and Django REST Framework that allows users to securely manage personal tasks

## Features
- User Authentication
- Create, Read, Update and Delete tasks
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

## Status
Version 0.1 — Core API endpoints implemented. Authentication coming next.

