install:
	pip install -U pip
	pip install -U setuptools
	pip install pipenv
	pipenv install --system --deploy --ignore-pipfile
