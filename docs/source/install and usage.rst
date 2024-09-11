Installation Guide
==================
.. raw:: html

   <br><br>

This guide will help you set up the OC Lettings project on your local machine.


Installation Steps
__________________

#. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/githubstevemas/Orange-County-Lettings.git

#. Create a virtual environment and activate:

   .. code-block:: bash

      python -m venv env

#. Activate the virtual environment:

   .. code-block:: bash

      env\Scripts\activate

#. Install the dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

#. Setup Environment Variables:
    In the ``.env`` file set environment variables like SECRET_KEY, Sentry DSN (If you don't have a Sentry account, sign up at `sentry.io <https://www.sentry.io>`_ and create a new Django project in your Sentry dashboard), and your host id.

6. Run Database Migrations:

   .. code-block:: bash

      python manage.py migrate

Usage
-----

1. Run the development server:

   .. code-block:: bash

      python manage.py runserver

2. Run the application:
    Open `http://localhost:8000 <http://localhost:8000>`_ in your browser.

3. Admin:
    Open `http://localhost:8000/admin <http://localhost:8000/admin>`_ and connect with user *admin*, password *Abc1234!*

.. note::
      The commands above are for Windows use. Go to the official `Python documentation <https://docs.python.org/3/tutorial/venv.html>`_ for MacOS or Unix usage.
