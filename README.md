# Django

## WHAT IS DJANGO?

Django is a full-featured web framework that simplifies the process of making web applications in Python. Note that Django is described as a framework and not a module or package. A framework is a collection of tools to aid you in web development. For example, you would create a model of data in Python. Django then converts the model to be used in a database. As a developer you do not need to worry about the conversion process. Django does this automatically.
Django uses the Model-View-Template (MVT) paradigm. The Model manages data, the view describes the subset of data sent to the user, and the template displays the data for the user. Underlying all of this is a URL pattern matching system. If a user goes to www.yourpage.com/about, Django will take the /about URL pattern and match it to a view, which is presented to the user.

FEATURES OF DJANGO FRAMEWORK

- PORTABLE
- SPEED
- SECURITY
- BATTERIES INCLUDED (ie., every library,tools required for a developer to build a web application)
- OPEN SOURCE 
- HUGE COMMUNITY
- SCALABILITY
- THOROUGHLY TESTED
- SUPERIOR FRAMEWORK DOCUMENTATION
- DRY PRINCIPLE (Don't Repeat Yourself)
- DJANGO'S ORM 
- ADMIN INTERFACE
- PACKAGES 

DJANGO ARE USED IN 

- NETFLIX
- INSTAGRAM
- CLUBHOUSE
- MOZILLA
- BITBUCKET
- SPOTIFY
- PINTEREST
- YOUTUBE

STARTING OUR DJANGO PROJECT

>>>django-admin startproject project_name

- Use the tree command to print a graphical representation of our current directory

>>>tree

Each file in the "beginner_project" directory serves a specific purpose

>>>asgi.py - this is an optional file used with an asynchronous server gateway interface
>>>__init.py__ - this indicates the directory is part of a python package
>>>settings.py - this file controls the settings for our django project 
>>>urls.py - this file tells the django which page to load when a user visits our site
>>>wsgi.py - the web server gateway interface is used when we host our site ona production server

NOTE : The manage.py file is not technically part of the django project since it is outside the beginner_project directory. But, this is a very important file, we will use it when we need to make migrations to the database, run our development server, etc.

Django automatically creates any files needed by the app. Each file has a specific purpose :

>>>admin.py - handles configuration of the built-in django
admin feature
>>>apps.py - handles configuration for the app itself
>>>migrations - the directory keeps track of changes to models so the databases stays in the sync
>>>models.py - handles the definition of database models
>>>tests.py - handles any tests specific to the app
>>>views.py - handles any HTTP requests and responses for the app

ADDING THE APP

django makes it really easy to add an app to the project, however is that the project "does not know" about the newly created app. We need to add our "languages" app to the list of "INSTALLED APPS" for the django project. Open "settings.py" then add our "languages" app to the end of the list.

With regards to Django, there are 2 kinds of webpages --- dynamic and static.
A dynamic website has content stored in a database. Users can alter the data in the database so the content displayed on the website can vary.
A static website does not rely on a database. All of the information is hardcoded in the file and does not change.

Django uses the MVT paradigm, so a dynamic website uses all of the four components : MODELS, VIEWS, TEMPLATES, URL pattern matching.
A static site only uses VIEWS, TEMPLATES, PATTERN MATCHING. 

The Model-View-Controller design pattern divides application logic into three components: 

          - Model accesses and manipulates data. 
          - View presents data in various forms. 
          - Controller coordinates between Model and View. 

The Django Model-View-Template pattern is like MVC, except that there is no Controller and the Django server itself performs the controller function. 

In Django, a View is a Python function that takes a Web request and applies the necessary logic to generate a Web response. 

Django uses a template containing static HTML elements and special Python code to generate dynamic Web pages.  

When you create a Django project, Django creates some core files. 

          - manage.py is a command-line interface used to interact with the Django project. 
          - settings.py contains the settings and configurations for your Django project. 
          - urls.py contains the URL and routing definitions of your Django app. 

You start building a Django admin site by creating an admin user. 

You can then log in as a superuser and register your models to the admin site so you can manage them. 

You can customize the admin form and add search and filters. 

A Django View takes a Web request such as HTTP GET, POST, DELETE, or UPDATE and returns a Web response. The web response can be a string, a JSON/XML file, an HTML page, or an error status indicating errors on the client or server-side. 

You create templates in Django to specify how your data will be presented. A Django template combines static HTML elements with Django template tags and variables to describe how the dynamic parts will be inserted. These work together to generate an HTML page that is rendered in a user’s web browser. 
