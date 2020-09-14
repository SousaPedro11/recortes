FROM python:alpine

LABEL maintainer="Pedro Sousa <ppls2106@gmail.com>"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN rm -rf /var/cache/apk/* && \
    apk update && \
    # apk add make && \
    # apk add build-base && \
    # apk add gcc && \
    # apk add libffi-dev && \
    # apk add musl-dev && \
    # apk add openssl-dev && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    # apk del build-base && \
    rm -rf /var/cache/apk/*

RUN pip install --upgrade pip
RUN pip install pipenv

RUN mkdir -p /home/api/

ENV HOME=/home/api/

RUN adduser -D api

WORKDIR $HOME

COPY Pipfile Pipfile.lock $HOME

RUN pipenv install --system --deploy --ignore-pipfile

COPY --chown=api:api . $HOME

RUN chmod +x ./startup.sh

EXPOSE 8001

USER api

CMD ["./startup.sh"]
#CMD python manage.py runserver 0.0.0.0:8001

# FROM python:3.8

# LABEL Name=recortes Version=0.0.1

# # env
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /code

# # pipenv

# RUN pip install --upgrade pip
# RUN pip install pipenv
# COPY Pipfile Pipfile.lock /code/
# RUN pipenv install --ignore-pipfile --system

# COPY . /code/

# RUN chmod +x ./run.sh

# EXPOSE 8000

# CMD ["./run.sh"]
