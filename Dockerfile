##Cloud Run serverless service vm, intall docker file (container run source code by dependece installation).
##its run all service with out compute resources
##docker file -->--> process --> doc file --> wok dir -->copy -->run --> txt req -->port externally
##Running program required program through docker file
##imported Docker images from Hub.docker.com
#sytax
FROM python:3.9.15-slim-bullseye
ENV PORT 8080
WORKDIR /ment360docker
COPY . /ment360docker
RUN pip install -r ment360requirement.txt
EXPOSE $PORT
CMD ["python", "flask_app.py"]
