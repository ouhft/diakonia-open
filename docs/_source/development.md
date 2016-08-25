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

[http://v4-alpha.getbootstrap.com]()




# Dev System Notes

## FHIRbase Install
On OS X 10.11.6, this has been a series of forward and backward steps. 

Homebrew supports the latest version of software, and one or two older versions. For FHIRbase to install locally we need the following stack:

* Postgres (v9.5.3 currently)
* FHIRbase(2) - [https://github.com/fhirbase/fhirbase-plv8]() (v1.4.0 currently)
* plv8 - [https://github.com/plv8/plv8 http://pgxn.org/dist/plv8/]()- (current is v1.5.3, but using v1.4.3 because it supports the older version of v8 available from the Homebrew Version archive)
* v8 - via Homebrew Versions archive - (current is v5.1; but using v3.15 as this is the only historic version at present available)

Can now condense this down to the following:

* `brew install v8-315` -- only works since June 2016
* `pip install pgxnclient`
* `LIBRARY_PATH="/usr/local/opt/v8-315/lib" CPATH="/usr/local/opt/v8-315/include" pgxnclient install plv8=1.4.3`
* Then we follow [https://github.com/fhirbase/fhirbase-plv8#installation]()
	* `psql -d postgres` -- because there isn't a DB named after the local user. We now are in the PSQL CLI:
	* `CREATE DATABASE fhirbase;`. Then exit CLI
	* `export DATABASE_URL=postgres://user:password@localhost:5432/fhirbase` -- remember to escape any symbols in password
	* `wget https://github.com/fhirbase/fhirbase-plv8/releases/download/v1.4.0.0/fhirbase-1.4.0.0.sql.zip`
	* `unzip fhirbase-1.4.0.0.sql.zip`
	* `cat fhirbase-1.4.0.0.sql | psql fhirbase`
* And it worked fine. Tested by creating patient storage, seeing new tables generated, and then removed the storage.


## Sphinx Install

Sphinx is configured to create documentation outputs ([#39](https://github.com/ouh-churchill/diakonia/issues/39)), and scan for django code. The html documentation is then pushed into another repository for display via GitHub pages ([#40](https://github.com/ouh-churchill/diakonia/issues/40))

To publish:

* In the diakonia repo, edit your documents, and commit changes
* From the cli, whilst **in the diakonia virtualenv**:
	* `cd docs`
	* `make html`
* In another cli, we add, commit, and push the changes to the documentation repo
	* `workon ouh-churchill-docs`
	* `cd ouh-churchill.github.io-repo`
	* `git add .`
	* `git commit -m 'updates'`
	* `git push`
	* For the quick, it can be: `git add .;git commit -m 'updates';git push`
* Online documents can then be seen at [https://ouh-churchill.github.io]()