FROM python:3.10.4-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
# RUN python manage.py migrate
CMD python manage.py migrate ; python manage.py runserver 0.0.0.0:8008

# ADD THIS CODE TO CREATE NEW SUPERUSER IN DJANGO ADMIN
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('USER', 'EMAIL', 'PASSWORD')" | python manage.py shell 