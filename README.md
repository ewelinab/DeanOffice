# DeanOffice

python3 -m venv myvenv
source myvenv/bin/activate
pip install --upgrade pip
pip install django~=1.10.0
git clone https://github.com/ewelinab/DeanOffice.git
cd DeanOffice
git checkout develop
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
