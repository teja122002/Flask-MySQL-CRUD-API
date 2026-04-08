# Flask MySQL CRUD API

A RESTful API built with Flask and MySQL that performs 
full CRUD operations on a Users resource. 
Tested with Postman.

## Tech Stack
- Python
- Flask
- MySQL
- Postman

## API Endpoints

| Method | Endpoint      | Description      |
|--------|---------------|------------------|
| POST   | /users        | Add new user     |
| GET    | /users        | Get all users    |
| GET    | /users/<id>   | Get single user  |
| PUT    | /users/<id>   | Update user      |
| DELETE | /users/<id>   | Delete user      |

## How to Run
1. Clone the repo
2. Install dependencies
   pip install flask mysql-connector-python
3. Create database in MySQL
   CREATE DATABASE testdb;
4. Run the app
   python main.py
5. Test in Postman → http://127.0.0.1:5000


Flask-MySQL-CRUD-API
