front:
	cd ./spbackend/spfrontend && npm run serve

back:
	python ./spbackend/manage.py runserver

run-lint:
	scripts/lint.sh