Installation Guide
==================
.. raw:: html

   <br><br>

This guide will help you set up the OC Lettings project on your local machine.

Requirements
____________

- Python 3.6 or higher
- Django 3.0

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

#. Apply migrations:

   .. code-block:: bash

      python manage.py migrate

#. Run the development server:

   .. code-block:: bash

      python manage.py runserver

.. note::
      The commands above are for Windows use. Go to the official `Python documentation <https://docs.python.org/3/tutorial/venv.html>`_ for MacOS or Unix usage.