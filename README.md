# django-customusermodel-boilerplate
Starter code on how to create django's custom user model that modifies on dajngo inbuilt user model with tests

## Usage

1. Clone the repo to your local directory
2. Make sure you have pipenv install so as to download the dependencies


```bash
$ pipenv install #  installs all packages from Pipfile including django.
$ pipenv shell #  Creates a virtual env.
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
(env)$ python manage.py test # to run the tests
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
