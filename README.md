# Discount Manager
The project allows you to manage a database with maps. The database stores card and purchase data.

## Getting Started  
The first thing to do is to clone the repository:  

```sh
$ git clone https://github.com/polina-koval/DiscountManager.git
$ cd DiscountManager
```  

Create a virtual environment to install dependencies in and activate it:  

```sh
$ virtualenv venv  
$ source venv/bin/activate
```

Then install the dependencies:  

```sh
(venv)$ pip install -r requirements.txt
```  

There is a file in the repo ".env.example", this file for use in local development. 
Duplicate this file as .env in the root of the project and update the environment 
variables SECRET_KEY, etc.  

```sh
$ cp .env.example .env
```

Once pip has finished downloading the dependencies and the variable is updated:  
 
Django:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py createsuperuser
(venv)$ python manage.py runserver
```

Navigate to [Main page with cards](http://127.0.0.1:8000/cards/)  and work with the existing cards.