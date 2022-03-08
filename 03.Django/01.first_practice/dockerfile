FROM python:3.6.5-slim
WORKDIR /app/src
RUN pip install Django==2.0.7
RUN django-admin startproject trydjango
CMD ["python", "./trydjango/manage.py", "runserver", "0.0.0.0:8000"]