FROM python:3.12-slim-bookworm

RUN python -m pip install --no-cache-dir pytest==9.1.1

WORKDIR /app/project
COPY parser.py /app/project/parser.py
COPY test_parser.py /app/project/test_parser.py
