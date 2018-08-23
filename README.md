# MemCachier and Django on Heroku tutorial

This is an example Django 2.1 task list app that
uses the [MemCachier add-on](https://addons.heroku.com/memcachier) on
[Heroku](http://www.heroku.com/). A running version of this app can be
found [here](http://memcachier-django-tasklist.herokuapp.com).

Detailed instructions for developing this app are available
[here](https://devcenter.heroku.com/articles/django-memcache).

## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Running Locally

Run the following commands to get started running this app locally:

```sh
$ git clone https://github.com/memcachier/examples-django-tasklist.git
$ cd examples-django-tasklist
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8000` to play with the app.

## Deploying to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/memcachier/examples-django-tasklist.git
$ cd examples-django-tasklist
$ heroku create
Creating app... done, ⬢ rocky-chamber-17110
https://rocky-chamber-17110.herokuapp.com/ | https://git.heroku.com/rocky-chamber-17110.git
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku addons:create memcachier:dev
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
```

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/examples-django-tasklist/issues).

Master [git repository](http://github.com/memcachier/examples-django-tasklist):

* `git clone git://github.com/memcachier/examples-django-tasklist.git`

## Licensing

This library is BSD-licensed.
