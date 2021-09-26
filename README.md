# DatJuanitaGurl

## Development

You will need to create a `.env` file to connect to the correct website. See `.envexample`.

Install libraries `pip install -r requirements.txt`.

## Docker Build

You can also build the Docker image. For example, run `docker build . -t datjuanitagurl/datjuanitagurl` to build the image. Then run `docker run --env-file ./.env datjuanitagurl/datjuanitagurl:latest` to run it.

## Full Application Usage

Clone and build `https://github.com/walleyyang/bad-bug`

Requires all the environment variables in `.envexample` in a new `.env`.

Run with `docker-compose up`.
