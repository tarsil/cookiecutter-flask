# {{ cookiecutter.description }} - {{ cookiecutter.project_name }}

* This template uses basic Flask [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* The requirements are located in `requirements.txt` and you can locally run `make requirements`. It will install the dev requirements as well.
* Uses cookiecutter to generate the template project

## Requirements

* Python 3.6 +
* (Optional) Virtualenv (or pyenv, venv...)
* Cookiecutter (to install the template)

## How to install

 1. Install cookiecutter. Instructions [here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)
 2. Run `cookiecutter https://github.com/tiagoarasilva/cookiecutter-flask` and follow the instructions

## Development

* The template offers a possibility to integrate with redis and postgres both locally and remotely, where remotely is up to the developer.
    1. Locally run `docker-compose up` and the service should trigger normally
    2. Remotely, replace settings (`config/settings.py`) with the settings you need

* If you wish to have other databases, just replace the variables by the ones necessary

# Run locally

* Run `make run-locally` or if you wish to run with a different set of settings:
    1. `make run-special FLASK_SETTINGS_FILENAME=_location_of_file/file.py`

* You should be able to access `http://127.0.0.1:5001/` and test the endpoint.


# Run tests

* Run `make run-tests`
