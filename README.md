# Wężowy czasooszczędzacz

This repository is the base on which I build the structures of my projects.

## Features

- `multi-stage` docker images
- `Docker Compose` with multiple compose files
- Monorepo-friendly structure
- `Poetry` for `Python 3.9`
- Prod stack: `Gunicorn` + `UvicornWorker`
- Dev stack: `Uvicorn` with shared code directory and autoreload

## How to use

1. Get repo
2. Think before modify
3. Modify
4. Think before use
5. Use
6. Enjoy the time saved

### Running development stack

``` sh
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

### Running "production" stack

``` sh
docker-compose -f docker-compose.yml up --build
```

## Useful documentation

- Docker: <https://docs.docker.com/>
- Docker Compose: <https://docs.docker.com/compose/>
- Poetry: <https://python-poetry.org/docs/>
- Uvicorn: <https://www.uvicorn.org/>
- Gunicorn: <https://docs.gunicorn.org/en/stable/index.html>
