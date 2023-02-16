FROM python:3.8.9

WORKDIR /server

COPY Pipfile Pipfile.lock pyproject.toml /server/

RUN apt-get -y install libc-dev
# RUN apt-get -y install build-essential
RUN pip install -U pip

RUN pip install pipenv && pipenv install --system --dev

COPY . /server/

EXPOSE 8000

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]