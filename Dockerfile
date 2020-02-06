FROM python:3.7

ARG CODE_LOCATION=/usr/app
ARG CODE_FOLDER=src

RUN mkdir -p ${CODE_LOCATION}/${CODE_FOLDER}/
WORKDIR ${CODE_LOCATION}

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ${CODE_FOLDER} ${CODE_FOLDER}

COPY ./manage.py .

CMD ["python","manage.py","worker"]

