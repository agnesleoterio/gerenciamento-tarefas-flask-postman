FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-interaction

COPY . .

EXPOSE 5000

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]