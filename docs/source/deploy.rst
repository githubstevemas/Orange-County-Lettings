Deploy
======

.. raw:: html

   <br><br>

The CI/CD pipeline will run automatically for every commit in the master branch using Github Actions and the ``ci.yml`` file present locally :
    - Flake8 and tests are run to verify that the code is robust and error-free (80% code coverage is required).
    - Then, using the ``Dockerfile``, a Docker image will be created and transferred to Docker Hub.
    - Finally the application is deployed on Render.

.. note::
      To ensure successful deployment, the following *GitHub Secrets* must be defined in the repository settings:
        - ``SECRET_KEY`` : Django secret key used for security.
        - ``DOCKER_HUB_USERNAME`` and ``DOCKER_HUB_PASSWORD`` : Credentials for Docker Hub.
        - ``RENDER_SERVICE_ID`` and ``RENDER_API_KEY`` : Credentials for Render.

        **Render Settings**:
            - The Render environment must be configured to pull the latest Docker image from Docker Hub.