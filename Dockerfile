##Running required programs through docker file
##imported Docker images from Hub.docker.com
FROM python:3.9.15-slim-bullseye
ENV PORT 8080
WORKDIR /ment360docker
COPY . /ment360docker
RUN pip install -r ment360requirement.txt
EXPOSE $PORT
CMD ["python", "flask_app.py"]
