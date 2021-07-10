db-run:
	python3 ./manage.py runserver

db-loaddata:
	python3 ./manage.py loaddata initial.yaml

db-migrate:
	python3 ./manage.py migrate

run-test:
	python3 ./manage.py test
