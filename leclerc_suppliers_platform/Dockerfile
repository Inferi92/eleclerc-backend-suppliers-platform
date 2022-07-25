FROM python:3.10.4-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD python manage.py makemigrations ; python manage.py migrate ; python manage.py runserver 0.0.0.0:8008; 

# ADD THIS CODE TO CREATE NEW SUPERUSER IN DJANGO ADMIN
# RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('telmo', 'seomanager@cooplecnorte.pt', '@Cooplec2022')" | python manage.py shell 
# 
