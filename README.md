<p align="center">
  <a href="https://o-c-lettings.readthedocs.io/en/latest/?badge=latest">
    <img src="https://readthedocs.org/projects/o-c-lettings/badge/?version=latest" alt="Documentation Status">
  </a>
  <img src="https://github.com/githubstevemas/Orange-County-Lettings/actions/workflows/ci.yml/badge.svg" alt="Build Status">
  <img src="https://codecov.io/gh/githubstevemas/Orange-County-Lettings/branch/master/graph/badge.svg" alt="Coverage">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python Version">
</p>


<br>

# Orange County Lettings

Django-based web application designed to manage property lettings and user profiles.

<br>

## Features

- **Lettings Management:** Manage lettings, including address information, and viewing details for specific lettings.
- **Custom Error Handling:** Implement custom 404 and 500 error pages with integrated Sentry error reporting.
- **Automated Testing:** Comprehensive test suite including unit tests for models, views, and URLs to ensure the reliability of the application.
- **Continuous Integration:** Integrated CI/CD pipeline using GitHub Actions, with checks for code quality, coverage, and linting before deployment.

<br>

## Technologies used

- **[Django](https://www.djangoproject.com/)**: A high-level Python web framework that promotes rapid development and clean, pragmatic design.
- **[Sentry SDK](https://docs.sentry.io/platforms/python/guides/django/)**: An error tracking tool that helps monitor and fix crashes in real-time, integrated with Django.
- **[Sphinx](https://www.sphinx-doc.org/en/master/)**: A documentation generator that converts reStructuredText files into various output formats like HTML and PDF.
- **[Requests](https://docs.python-requests.org/en/latest/)**: A simple HTTP library for Python, used to make HTTP requests within the project.
- **[SQLParse](https://sqlparse.readthedocs.io/en/latest/)**: A library for parsing and formatting SQL statements, used in database-related operations.

<br>

## Prerequisites

- [Github](https://www.github.com) to clone the project.
- [Sentry](https://www.sentry.io) for monitoring and error traking.
- [Docker](https://www.docker.com) for containerized deployment.
- [Render](https://www.render.com) (or any other) to host.

<br>

## Install and configuration


*Clone the repository :*
```
git clone https://github.com/githubstevemas/Orange-County-Lettings.git
cd Orange-County-Lettings
```

*Install a new vitual environement and activate :*
```
python -m venv env
env/Scripts/activate
```

*Install all the depedencies :*
```
pip install -r requirements.txt
```

*Setup Environment Variables :*

In the ``.env`` file set environment variables like SECRET_KEY, Sentry DSN (If you don't have a Sentry account, sign up at [sentry.io](https://www.sentry.io) and create a new Django project in your Sentry dashboard), and your host id.

*run Database Migrations :*
```
python manage.py migrate
```

<br>

## How to run
*Once the project configuration is completed you can execute the following commands in the project folder to start server :*
```
python manage.py runserver
```

Now, visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the app locally.



<br>

> [!NOTE]
> The commands above are for Windows use. Go to the official [Python documentation](https://docs.python.org/3/tutorial/venv.html) for MacOS or Unix usage.

<br>


## Usage

*Run the application :*
```
python manage.py runserver
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

<br>

## Admin

Open [http://localhost:8000/admin](http://localhost:8000/admin) and connect with user *admin*, password *Abc1234!*

<br>


## Run Tests

*Before running the tests, ensure all dependencies are installed and migrations are applied. Then, run the following command :*
```
coverage run -m pytest -s
coverage rpport
```
This will execute all tests found in the directories within the app and displays the code coverage rate.

<br>


## Running Flake8

*You can run flake8 to check your code for any style violations :*
```
flake8 .
```
This will check all the files for PEP8 compliance and other issues.

<br>

## Deploy

The CI/CD pipeline will run automatically for every commit in the master branch using Github Actions and the ``ci.yml`` file present locally :
- Flake8 and tests are run to verify that the code is robust and error-free (80% code coverage is required).
- Then, using the ``Dockerfile``, a Docker image will be created and transferred to Docker Hub.
- Finally the application is deployed on Render.

> [!NOTE]
> To ensure successful deployment, the following *GitHub Secrets* must be defined in the repository settings:
> - ``SECRET_KEY`` : Django secret key used for security.
> - ``DOCKER_HUB_USERNAME`` and ``DOCKER_HUB_PASSWORD`` : Credentials for Docker Hub.
> - ``RENDER_SERVICE_ID`` and ``RENDER_API_KEY`` : Credentials for Render.
> - Also, the Render environment in your Dashboard must be configured.

<br>

## Troubleshooting

- **500 Internal Server Error :** verify that the SECRET_KEY is not missing or incorrectly set.
- **400 Error :** verify that ALLOWED_HOST in ``settings.py`` is not missing or incorrectly set.
- **Database Migration Issues :** run python ``manage.py migrate to apply`` the database migrations.
- **Static Files Not Loading :** ensure that collectstatic has been run successfully.
- **Deployment Failure :** ensure that the RENDER_SERVICE_ID, DOCKER_HUB_USERNAME, and DOCKER_HUB_PASSWORD are properly configured in GitHub Secrets.

<br>

## Changelog

### [Version 2.0]
- Reorganizing code into several separate applications.
- Moving site HTML files into specific template folders with each application.
- Fixing linting errors.
- Handling 404 and 500 errors.
- Code documentation.
- Setting up unit tests.
- Application monitoring and tracking errors via Sentry.
- Setting up a deployment pipeline.

<br>

This project is a fork of [Python-OC-Lettings-FR](OpenClassrooms-Student-Center/Python-OC-Lettings-FR).

## Contact
Feel free to [mail me](mailto:mas.ste@gmail.com) for any questions, comments, or suggestions.
