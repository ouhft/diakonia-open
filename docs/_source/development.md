# Project Setup Notes

Starting with notes from [https://github.com/AllyBradley/COPE/blob/master/docs/deployment.rst]() and `development.rst`. Note that development doesn’t talk about starting a new project with virtualenv!

Need to make a project directory using python 3.5.2 (latest as of time of writing)
[http://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv]()

* `mkproject -p /usr/local/bin/python3 diakonia`

Results in us going to `/Users/$USER$/Projects/diakonia`

Create a project on github : [https://github.com/ouh-churchill/diakoinia](), then clone it…

* `git clone git@github.com:ouh-churchill/diakonia.git diakonia-repo`
* `ln -s ~/.virtualenvs/diakonia/lib ./lib`
* `ln -s ~/.virtualenvs/diakonia/bin ./bin`

Open project in PyCharm, and create requirements file (`requirements/common.txt` and `development.txt`).

* `pip install -r diakonia-repo/requirements/development.txt`

## Creating the intial project

Start the django project:

* `cd diakonia-repo`
* `django-admin startproject diakonia`

Then move some things around…

* Move `manage.py` to `diakonia-repo/`
* Move and rename `diakonia/` to `diakonia-repo/config/`
* Edit `manage.py` and `wsgi.py` to point at `“config.settings”`

After that, PyCharm will want a few settings tweaks (like Django support enabling, and pointing at the settings files). I tend to hold of on this until I've also sorted out the setup of Best Practice for settings and other folders/files that form part of the project boilerplate.



http://v4-alpha.getbootstrap.com




