install:
	uv sync
build:
	./build.sh
collectstatic:
	uv run python3 manage.py collectstatic --noinput
migrate:
	uv run python3 manage.py migrate
lint:
	uv run ruff check
render-start:
	uv run gunicorn task_manager.wsgi

.PHONY: install build collectstatic migrate lint render-start
