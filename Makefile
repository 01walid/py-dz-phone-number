## default target, lists what to do when you type "make" without any target.
default: 
	@echo "Choose a target:"
	@echo "  make install - installs dev dependencies." 
	@echo "  make test - test the project with pytest." 
	@echo "  make format - formats the project using Black." 
	@echo "  make build-dist - Generates Python distribution archives." 
	@echo "  make release - uploads the archives to pypi.org (making it pip installable)." 

install:
	# If you're not inside a virtual environment, you might want to add --user:
	# pip install --user -e ".[dev]"
	pip install -e ".[dev]"

test:
	python3 -m pytest 

format:
	@echo "Formatting code with Black.."
	black .

build-dist:
	pip install --user --upgrade setuptools wheel
	rm -vrf ./build ./dist ./*.egg-info
	python3 setup.py sdist bdist_wheel

release: build-dist
	pip install --user --upgrade twine
	twine upload dist/*
