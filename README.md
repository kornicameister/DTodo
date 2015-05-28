# DTodo Showcase project

## Prerequisites

In order to successfully start the application following things need to be installed
in OS:
* Python 3.4.x [link](https://www.python.org/ftp/python/3.4.3/python-3.4.3.msi)
* PIP (Python Package Manager), already bundled in Python 3.4.x

## Installation of required packages

Project has several dependencies that need to be installed in the OS
before continuing thus from the root of the project execute following command
in shell

```
pip install -r requirements.txt
```

This will install all libraries defined in file **requirements.txt**

## Preparing to start up the application

### Database

Next execute following commands to apply all changes that have been applied
on the database

```
python manage.py migrate
```

### Compiling translations

Execute this command from the root of the project
```
python manage.py compilemessages
```

### Client side libraries

Application uses several libraries in the client side, they are 
managed with [bower](http://bower.io/) package manager.

If bower is already installed, just execute following command from
the root of the project

```
bower install
```

If bower is not available in OS follow this [instruction](http://bower.io/#install-bower). 
Installation of bower is available while having:
* NodeJS
* NPM 
* GIT
These requirements must be met before installing *bower*.

## Running application

Simply execute this command from root of the project
```
python manage.py runserver
```
