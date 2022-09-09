# Garby - garbage report and earn
python Django Tailwind Twilio CockroachDB


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/techakhil-me/garby
$ cd garby
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate   (mac/linux)
$ venv/Sripts/activate  (windows)
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd garby
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

# Garby prototype
check the prototype here <a href="https://garby.anikacp.repl.co/" target="_blank">GARBY</a>
