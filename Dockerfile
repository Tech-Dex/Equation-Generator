FROM python:3

ENV PYTHONNUNBUFFERED 1
ENV PYTHONPATH "/app"

ENV DB_USER "root"
ENV DB_USER_PASSWORD "pass"
ENV HOST "172.17.0.2"
ENV PORT "3306"
ENV DATABASE "math"
ENV TABLE "equations"


RUN mkdir /app
WORKDIR /app
ADD . /app

RUN apt-get update
RUN pip install -r requirements.txt

#CMD ["main.py"]
#ENTRYPOINT ["python3"]