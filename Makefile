install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
lint:
	poetry run flake8 brain_games
reinstall:
	rm -r dist
	poetry build
	python3 -m pip install --user dist/*.whl --force-reinstall
asci:
	clear
	asciinema rec
push:
	git push git@github.com:bapplesova/python-project-lvl1.git
