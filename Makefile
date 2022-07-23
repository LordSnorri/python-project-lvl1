build: #building from poetry build
	poetry build

publish: #publishing said build using dry-run
	poetry publish --dry-run

package-install: #installing package to the system 
	python3 -m pip install --user dist/*.whl
