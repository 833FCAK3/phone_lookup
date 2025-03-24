run:
	python manage.py runserver

project:
	django-admin startproject $(a)
	# django-admin startproject mysite djangotutorial

app:
	python manage.py startapp $(a)

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell

collectstatic:
	python manage.py collectstatic
