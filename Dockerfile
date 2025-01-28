FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY init.sh entrypoint.sh
COPY . .

RUN python3 -m venv ambient \
    && ./ambient/bin/pip install --upgrade pip \
    && ./ambient/bin/pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["bash", "/app/entrypoint.sh"]
