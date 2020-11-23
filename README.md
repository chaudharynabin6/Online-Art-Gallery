# Online-Art-Gallery
This project is dedicated to minor project of Sagarmatha Engineering College. 
## project uses following tools
* django
* postgresql
* semantic-ui
* jquery
# Dependencies
> * you can find of  most dependencies on pipfile
> * you must install prostgress and setup the username,database,and password from [how to setup postgresql for django in windows](https://medium.com/@9cv9official/creating-a-django-web-application-with-a-postgresql-database-on-windows-c1eea38fe294)
> * you must enable pg_tgrm extension on postgres sql just like this video from [install extension in postgresql](https://www.youtube.com/watch?v=afK8GWpb8RU)
> * for frontend [semantic-ui](https://semantic-ui.com/) is used
> * most of other fronend stuff cdn links are used

# Note
> *note: the development environment is windows. some of the hash value of pipfile.lock may not be compatible with linux in that case you must delete that pipfile.lock for compatibility and install the project*


# installation guide
**Follow the steps for project setup**

> 1. Choose project folder
> 2. In terminal run: `pip3 install pipenv`
> 3. Enter the folder with virtual environment: `cd name`
> 4. Activate virtual environment : `python -m pipenv shell`
> 5. Go to the source folder : `cd src`
>6. Do the migration : `python manage.py migrate`
> 7. Create super user : `python manage.py createsuperuser`
> 8. Test the server: `python manage.py runserver`
> 9. go to this url in the browser: http://127.0.0.1:8000/
