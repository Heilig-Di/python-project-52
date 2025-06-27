build:
	chmod +x ./build.sh && ./build.sh
install:
	pip install uv && uv pip install -e .
collectstatic:
	python3 manage.py collectstatic --noinput
migrate:
	python3 manage.py migrate
lint:
	uv run ruff check
render-start:
	gunicorn task_manager.wsgi:application

.PHONY: build install collectstatic migrate lint render-start
