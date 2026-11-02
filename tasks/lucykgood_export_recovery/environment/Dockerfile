FROM python:3.12-slim-bookworm

RUN python -m pip install --no-cache-dir pytest==9.1.1

WORKDIR /app
COPY config.json /app/config.json
COPY HANDOFF.md /app/HANDOFF.md
COPY data/ /app/data/
COPY tools/ /app/tools/
