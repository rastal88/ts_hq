FROM python:3.10

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

RUN useradd -rms /binbash ts && chmod 777 /opt /run

WORKDIR /ts

COPY --chown=ts:ts core .
RUN pip install -r requirements.txt

USER st


CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]