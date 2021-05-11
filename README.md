# myDjangoBlog

This is my personal project about my porfolio and blog

These are steps to install and setting up the project;

Install Django at command line in powershell: pip install Django
show the list of django webapp by: django-admin
Start to create a project the project: django-admin startproject 'name of project' ---> cd point to the project

Part 1: set up the project
- Start the project: python manage.py runserver
- Now, we can go to localhost:8000 or http://127.0.0.1:8000/ to check the server
- Now start to create blog app by: python maange.py starapp blog (here 'blog' the name of the app)
- Go to views.py and import HTTP response by: from django.http import HttpResponse
- Next, add include to urls.py of the main project.

-----------------------------
Part 2: use templates
- Go to apps.py
Part 3:
Create an admin account to login the server by command:
- python manage.py createsuperuser 
- python manage.py makemigrations
- python manage.py migrate
- 'python manage.py sqlmigrate blog 0001' to save database
- rerun the command: manage.py createsuperuser
Part 4:
User python manage.py shell
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> Post.objects.all()
>>> creat a User after login again: user = User.objects.filter(username='brianhuynh').first()
- Save metho post_2.save()
- post.author.email >>> 'huynh2102@gmail.com'
- Get all the posts: user.post_set.all()


*notes:
Doing with Django
*
1. set up virtual environment.

step 1: python -m venv --system-site-package 'name of the directory' or python -m venv
ex: python -m venv myblog_env

step 2: source project_env/bin/activate
ex: source myblog_env/bin/activate

step 3: pip list and install other tool/programs
step 4: pip freeze > requirements.txt
step 5: deactivate

*In case that you wanna delete the environment, so we use: rm -rf 'name of the environment'

cd !$ go to the project

--------------
