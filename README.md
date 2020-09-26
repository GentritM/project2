# project2


delete the venv directory
create new virtualenv
activate it
install the reqs with:
$pip install -r requirements.txt

delete engage.db

create new db file and copy the full path

at app.py database configuration change the db path with your db file path

run:
$python app.py db init
$python app.py db migrate
$python app.py db upgrade

then:
$python app.py runserver
