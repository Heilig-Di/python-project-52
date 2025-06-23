build:
        ./build.sh
install:
	uv sync
render-start:
	gunicorn task_manager.wsgi
