### Installation and Packages

- Python 3.8.11
```
python --version
```

- Django 
```
pip3 install 'django<4'
```

- Create a new Django project
```
django-admin startproject django_todo .
```

- Run the project
```
python3 manage.py runserver
```

- Create a app
```
python3 manage.py startapp <appname>
```

## Heroku

1. Step One:
```
curl https://cli-assets.heroku.com/install.sh | sh
```

2. Step Two: Login:
```
heroku login -i
```

3. Enter With email and password
```
email: <enter_email>
password: <enter_password>
```

4. Psycopg2 package for Database:
```
pip3 install psycopg2-binary
```

5. Install webserver for deplyoment:
```
pip3 install gunicorn
```

6. Create `requirements` file:
```
pip3 freeze --local > requirements.txt
```

7. Create Heroku App:
```
heroku apps:create <ck28780-first-django-app> --region eu
```

8. Setting up Heroku Databse:
```
heroku addons:create <name_of_addon>
```

It's preferred to add this on the GUI but after thats done to check that it's installed then type:
```
heroku addons
```

**If you get the error below during the steps to deployment:**
```
django.db.utils.OperationalError: FATAL: role "somerandomletters" does not exist
```
**Please run the following command in the terminal to fix it:**
```
unset PGHOSTADDR
```
9. Connect to the Database:

**Important Note**: 

It's important to make sure that your Python package versions are compatible.
As we are using Django 3.2, we need to use the correct version of dj-database-url
```
pip3 install dj_database_url==0.5.0
```
Then after insatlling this oackage add it to the `requirements.txt`
```
pip3 freeze --local > requirements.txt
```
We need to get our `URL` for the `db`:

```
heroku config
```

you will recieve a `DATABASE_URL`

Then access `settings.py` and look for the `DATABASE` value, then:

```
DATABASES = {
    'default': dj_database_url.parse('<DATABASE_URL>')  # noqa
}

```

Then don't forget to `import` the:
```
import dj_database_url
```

We need to then run migrations:
```
python3 manage.py migrate
```
10. Pushing our changes to github
```
git push origin master
```

11. Attempting First Deployment to Heroku
```
git push heroku main
```

12. Create `Procfile`
```
web:gunicorn <django_todo>.wsgi:application
```