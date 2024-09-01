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

## How to run
Once the code has been downloaded, go to the project directory and enter the following commands in terminal

*install a new vitual environement :*
```
python -m venv env
```
*activate the environement :*
```
env/Scripts/activate
``` 
*install all the depedencies :*
```
pip install -r requirements.txt
```

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

## Contact
Feel free to [mail me](mailto:mas.ste@gmail.com) for any questions, comments, or suggestions.
