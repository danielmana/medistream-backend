medistream-backend
====================================

Project created using [seed](https://github.com/zackargyle/angularjs-django-rest-framework-seed) for a cross domain Angularjs / Django Rest Framework Application

    INCLUDED
        - RESTFUL API service for Medistream models
        - Login to obtain django token

After cloning down the repository:

1.  pip install fabric
2.  fab install:version=2.7 (or whatever version of python you are using)
3.  You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? no
       - The authtoken table is not created yet, so be sure to respond no to this request.
4.  Setup your superuser

Bam, you're good to go.

Afterwards, to see it in action, here is a simple way:

1.	python manage.py runserver 8001
2.	Open browser to http://localhost:8001/admin

Please give feedback, or bug fixes.

<br>

    NOTES: 
    
    - I highly suggest using a virtualenv as to not mess with in-built dependencies

    - Check out
      1. http://django-rest-framework.org/
      2. http://angularjs.org/
