build:
	./build.sh
install:
	uv pip install .
collectstatic:
	python3 manage.py collectstatic --noinput
migrate:
	python3 manage.py migrate
lint:
	uv run ruff check
render-start:
	gunicorn task_manager.wsgi

.PHONY: build install collectstatic migrate lint render-start
