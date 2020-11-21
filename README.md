# {{ cookiecutter.description }} - {{ cookiecutter.project_name }}

[![CircleCI](https://circleci.com/gh/tarsil/cookiecutter-flask.svg?style=shield&circle-token=dc7b04e09667d387047c4b59faa604a22867189b)](https://circleci.com/gh/tarsil/cookiecutter-flask)

- This template uses basic [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- The requirements are located in `requirements.txt` and you can locally run `make requirements`. 
It will install the dev requirements as well.
- Uses cookiecutter to generate the template project

---

## Table of Contents

- [Requirements](#requirements)
- [How to install](#how-to-install)
- [Development](#development)
- [Run Locally](#run-locally)
- [Run Tests](#run-tests)

---

## Requirements

- Python 3.6 +
- (Optional) Virtualenv (or pyenv, venv...)
- Cookiecutter (to install the template)
- Docker (optional and latest) and docker-compose (also optional and latest)

## How to install

 1. Install cookiecutter. Instructions [here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
 2. Run `cookiecutter https://github.com/tiagoarasilva/cookiecutter-flask` and follow the instructions
 3. `make requirements` - Installs all the requirements needed.

## Development

- The template offers a possibility to integrate with redis and postgres both locally and remotely, 
where remotely is up to the developer.
    1. Locally run `docker-compose up` and the service should trigger normally
    2. Remotely, replace settings (`config/settings.py`) with the settings you need

- If you wish to have other databases, just replace the variables by the ones necessary

## Run locally

- make run-local` or if you wish to run with a different set of settings:
    1. `make run-special FLASK_SETTINGS_FILENAME=_location_of_file/file.py`

- You should be able to access `http://127.0.0.1:5001/` and test the endpoint.

## Run tests

- `make run-tests` - Runs all the standard tests
