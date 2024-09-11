Troubleshooting
===============

.. raw:: html

   <br><br>

- 500 Internal Server Error:
    Verify that the SECRET_KEY is not missing or incorrectly set.
- 400 Error :
    Verify that ALLOWED_HOST in settings.py is not missing or incorrectly set.
- Database Issues:
    Run python ``manage.py migrate to apply`` the database migrations.
- Static Files Not Loading:
    Ensure that collectstatic has been run successfully.
- Deployment Failure:
    Ensure that the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DOCKER_HUB_USERNAME, and DOCKER_HUB_PASSWORD are properly configured in GitHub Secrets.