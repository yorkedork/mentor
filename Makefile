.PHONY: run clean install deploy prod dev

DEFAULT_DB_NAME=mentor
WSGI_PATH=mentor/wsgi.py
GIT_REMOTE=git@github.com:PSU-OIT-ARC/mentor.git
DEV_PATH=/vol/www/mapsmentors/dev
PROD_PATH=/vol/www/mapsmentors/prod


PYTHON=python3
export PATH:=.env/bin:$(PATH)


run: .env
	python manage.py runserver 0.0.0.0:8000

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete
	find . -iname "__pycache__" -delete

deploy: .env
ifdef BRANCH
	git remote set-url origin $(GIT_REMOTE_HTTPS)
	git remote update
	git fetch --all
	git merge --ff-only origin/$(BRANCH)
endif
	python manage.py migrate
	python manage.py loaddata choices
	python manage.py collectstatic --noinput
	touch $(WSGI_PATH)

install: .env
	mysql -e "CREATE DATABASE IF NOT EXISTS $(DEFAULT_DB_NAME)"
	python manage.py migrate
	python manage.py loaddata choices

.env: requirements.txt
	$(PYTHON) -m venv .env
	curl https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py | python
	pip install -r requirements.txt

dev:
	git push $(GIT_REMOTE) HEAD:master
	ssh -t hrimfaxi.oit.pdx.edu "sudo bash -c 'cd $(DEV_PATH) ; make BRANCH=master deploy'"

prod:
	git push $(GIT_REMOTE) HEAD:prod
	ssh -t hrimfaxi.oit.pdx.edu "sudo bash -c 'cd $(PROD_PATH) ; make BRANCH=prod deploy'"
