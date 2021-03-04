# Equation Generator

A simple equation generator. This generator was created and used for a CS:GO server (JB.GGEZ.RO) to implement an interactive activity with rewards and is used as an API. The API is used outside of the CS:GO server because we want to keep it as fast as possible and not to fill it with a lot of logic. The only thing that CS:GO is doing is to query the database from time to time for an equation.


## Setup with docker
1. ### Edit Dockerfile
 ```docker
 FROM python:3

ENV PYTHONNUNBUFFERED 1
ENV PYTHONPATH "/equation-generator"

ENV DB_USER "YOUR_USER"
ENV DB_USER_PASSWORD "YOUR_PASSWORD"
ENV HOST "YOUR_HOST"
ENV PORT "3306"
ENV DATABASE "YOUR_DATABASE"
ENV TABLE "YOUR_TABLE"
ENV TIMER "60"
ENV MIN_COEFFICIENTS "4"
ENV MAX_COEFFICIENTS "10"
ENV MIN_COEFFICIENT_VALUE "1"
ENV MAX_COEFFICIENT_VALUE "30"
ENV MIN_COEFFICIENT_VALUE_SPECIAL "1"
ENV MAX_COEFFICIENT_VALUE_SPECIAL "10"
ENV MIN_EQUATIONS_IN_DB "10"
ENV EQUATIONS_TO_PUSH_IN_DB "1000"

RUN mkdir /equation-generator
WORKDIR /equation-generator
ADD . /equation-generator

RUN apt-get update
RUN pip install -r app/requirements.txt

CMD ["app/main.py"]
ENTRYPOINT ["python3"]
```
2. ### Build and run dokcer
 ```bash
docker build . -t docker_name
docker run -dt --restart unless-stopped docker_name
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to test before pull request.

## License
[MIT](https://choosealicense.com/licenses/mit/)
