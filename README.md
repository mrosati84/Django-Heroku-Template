# Django 1.5 template for Heroku

-------

This project aims to be a super-simple starter Django project ready to be deployed in Heroku. The only steps to be ready to go are these:

1. use ``virtualenv`` to provide a virtual environment for this new project
2. install ``Django`` (omit this step if you have installed it gobally on your system)
3. create a new project with ``django-admin.py`` using this repo as template
4. install project dependencies using ``pip``

## Creating a virtual environment

To start over, first of all create a new empty directory. We will call it ``myproject``, and cd into it

    user@host:$ mkdir myproject && cd myproject

Now create a new virtual environment into it. We will call it ``venv`` as this directory name is already included in project's ``.gitignore`` file. Next activate the environment.

    user@host:$ virtualenv --distribute venv
    user@host:$ source venv/bin/activate
    (venv)user@host:$

It's time to install Django: if you have it already installed on your system skyp this step, else:

    (venv)user@host:$ pip install Django

## Creating the project

We can finally create the project using ``django-admin.py``

    (venv)user@host:$ django-admin.py startproject myproject --template http://<url> .

Please not the final dot ``.``, this indicates that the project has to be placed in the current directory, without creating a container directory called ``myproject``.

### Project set-up

The setting for this new project are located in the project directory ``myproject``. As you will see, there are two settings files: ``localsettings-dist.py`` and ``prodsettings.py``.
The first one needs to be copied to ``localsettings.py`` and must contain your environment-specific settings (database, secret key, etc.). The second will contain your global setting (paths, applications, middleware, etc).

Be sure to create a ``localsettings.py`` file, or the development server will run into an error at the first run.

### Setting up Heroku
