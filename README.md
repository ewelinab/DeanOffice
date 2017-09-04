# DeanOffice

python3 -m venv myvenv
source myvenv/bin/activate
pip install --upgrade pip
pip install django~=1.10.0
git clone https://github.com/ewelinab/DeanOffice.git
cd DeanOffice
git checkout develop
python manage.py migrate
python manage.py makemigrations deanOffice
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


--------------------
mysql
--------------------
sudo apt-get update
sudo apt-get install mysql-server
pip install PyMySQL
----
mysql -u root -p
CREATE DATABASE deanofficedatabase;
----
python manage.py migrate
python manage.py makemigrations deanOffice
python manage.py migrate
python manage.py runserver
----
http://localhost:8000/fillDatabase/
----


--------------------
postgresql
--------------------
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
pip install psycopg2
--------------------
sudo su - postgres
psql
CREATE USER root WITH PASSWORD 'root';
ALTER ROLE root SET client_encoding TO 'utf8';
ALTER ROLE root SET default_transaction_isolation TO 'read committed';
ALTER ROLE root SET timezone TO 'Europe/Warsaw';
CREATE DATABASE deanofficedatabase;
GRANT ALL PRIVILEGES ON DATABASE deanOfficeDatabase TO root;
\q
exit
---------------------
python manage.py migrate
python manage.py makemigrations deanOffice
python manage.py migrate
python manage.py runserver
---------------------
http://localhost:8000/fillDatabase/
---------------------
https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

--------------------------------------