FROM python:3.12-slim

WORKDIR /app

COPY library/pyproject.toml .

RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir .

COPY . .

WORKDIR /app/frontends

ENV PYTHONPATH="${PYTHONPATH}:/app:/app/library:/app/library/src"

ENTRYPOINT ["python", "-m", "console", "-X", "minimax"]
CMD ["-O", "minimax"]

#CMD  python -m console -X minimax -O minimax