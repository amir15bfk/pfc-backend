# pfc-backend
## requerments
```
pip install django
pip install djangorestframework
pip install pyjwt
pip install drf-yasg
```
### or
```
pip install -r requerments.txt
```
## init database
```
cd pfc
python manage.py makemigrations
python manage.py migrate
```
## start server
```
cd pfc
python manage.py runserver 1.1.1.1:8000
```
## create superuser (admin) to entre the admin panel
```
python manage.py createsuperuser
```
