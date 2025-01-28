FROM python:3.10

COPY requirements.txt requirements.txt
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

# copia o código do app para o conteiner
COPY . .

RUN python3 -m venv ambient && . ambient/bin/activate \
&& pip install -r requirements.txt

ENTRYPOINT ["bash", "/entrypoint.sh"]