FROM python:3.11

# Não utilizar arquivos .pyc na construção da imagem/contêiner
ENV PYTHONDONTEWRITEBYTECODE 1

# Não utilizar buffer de saída padrão. Os logs de erro não se perdem entre a aplicação e o contêiner
ENV PYTHONUNBUFFERED 1

WORKDIR /django_app

COPY . /django_app

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]