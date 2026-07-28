FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIPENV_VENV_IN_PROJECT=0 \
    PIPENV_DONT_USE_PYENV=1 \
    PIPENV_SYSTEM=1

WORKDIR /app

RUN pip install --no-cache-dir pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY mysite/ ./mysite/

WORKDIR /app/mysite

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
