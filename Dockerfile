FROM python:3

ENV PYTHONNUNBUFFERED 1
ENV PYTHONPATH "/equation-generator"

ENV DB_USER "root"
ENV DB_USER_PASSWORD "pass"
ENV TIMER "60"
ENV HOST "172.17.0.2"
ENV PORT "3306"
ENV DATABASE "math"
ENV TABLE "equations"


RUN mkdir /equation-generator
WORKDIR /equation-generator
ADD . /equation-generator

RUN apt-get update
RUN pip install -r app/requirements.txt

CMD ["app/main.py"]
ENTRYPOINT ["python3"]
