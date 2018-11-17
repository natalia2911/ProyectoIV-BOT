FROM python:3

MAINTAINER Natalia Mártir <nataliamartir@correo.ugr.es>
WORKDIR src/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


COPY requirements.txt ./
EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "noticiero-app:app"]
