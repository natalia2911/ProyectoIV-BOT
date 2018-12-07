FROM python:3

MAINTAINER Natalia <nataliamartir@correo.ugr.es>
WORKDIR src/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD cd src && gunicorn noticiero-app:app --bind 0.0.0.0:80
