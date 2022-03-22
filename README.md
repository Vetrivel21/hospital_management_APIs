# hospital_management_APIs
# Steps to install Django application and creating a project.
1. Download and install python version 3.10.1. 
2. Download and install Pycharm IDE.
3. Initially install python in system and configure the python interpreter in pycharm settings.
4. Specify the path where the project has to be created.
5. Install Django of version 3.9.10 in pycharm using the command: pip install django
6. Create a new project in django using the command: django-admin startproject student_management_system
7. Create a app in django using the command: python manage.py startapp student
8. Create the admin by using the command: python manage.py createsuperuser
9. Run the project using the command: python manage.py runserver

# Steps to run the project
1. Install python and pycharm IDE for running the project.
2. Open the terminal and execute following commands.
3. Install dependencies: pipenv install (This will create a virtual environment and install all depedencies).
4. Activate the virtual environment: pipenv shell
5. Configure the valid python interpreter for running the project.
6. Follow the commands:
   * pip install djangorestframework
   * Add "rest_framework" in the Installed apps in settings.py file.
   * py manage.py makemigrations
   * py manage.py migrate
8. Run the app: python manage.py runserver
9. Enter following URL in Your Browser or postman with url endpoints and send the request.
http://127.0.0.1:8000/

# Requirements
asgiref==3.5.0
certifi==2021.10.8
cffi==1.15.0
charset-normalizer==2.0.10
colorama==0.4.4
coreapi==2.3.3
coreschema==0.0.4
cryptography==36.0.1
defusedxml==0.7.1
Django==3.2.10
django-rest-knox==4.1.0
django-safedelete==1.1.2
django-templated-mail==1.1.1
djangorestframework==3.13.1
djangorestframework-simplejwt==4.8.0
djoser==2.1.0
hospital==0.9
httpie==3.1.0
idna==3.3
itypes==1.2.0
Jinja2==3.0.3
MarkupSafe==2.0.1
multidict==6.0.2
oauthlib==3.2.0
psycopg2==2.9.3
pycparser==2.21
Pygments==2.11.2
PyJWT==2.3.0
PySocks==1.7.1
python3-openid==3.2.0
pytz==2021.3
requests==2.27.1
requests-oauthlib==1.3.1
requests-toolbelt==0.9.1
six==1.16.0
social-auth-app-django==4.0.0
social-auth-core==4.2.0
sqlparse==0.4.2
tzdata==2021.5
uritemplate==4.1.1
urllib3==1.26.8


