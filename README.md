# Restaurant Manager
**!! Still in progress and not working proper !!**

It is a fictional website to manage restaurants and their menus. The Code is to test and combine concepts from the udacity Full Stack Web Developer Nanodegree Program.

### Tech

Restaurant Manager uses follwing open source projects:

* [Flask](http://flask.pocoo.org/) - is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)- is an extension for Flask that adds support for SQLAlchemy to your application
* [oauth2client](https://github.com/googleapis/oauth2client)-This is a Python library for accessing resources protected by OAuth 2.0.

### Installation and run

Install the dependencies
```sh
$ pip install flask
$ pip install oauth2client
$ pip install flask_sqlalchemy
```
Run the following python scripts to create and fill the sql database
```sh
$ python CreateDbAndContent.py
```
To run the WebApp 
```sh
$ python run.py
```
The site is running on http://127.0.0.1:5000/
### License
MIT
