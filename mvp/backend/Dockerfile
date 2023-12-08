# Use a imagem base Python 3.10
FROM python:3.10.12

# Informações do mantenedor
LABEL maintainer "Eduardo Iotti <ddz.iotti@gmail.com>"

# Atualize e instale pacotes necessários
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-venv \
    python3-wheel \
    && apt-get clean

# Crie o diretório /backend e defina como diretório de trabalho
RUN mkdir /backend
WORKDIR /backend

# Copie o código fonte do aplicativo para o contêiner
COPY . /backend

# Instale as dependências do aplicativo
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 5000
EXPOSE 5000

# Comando para iniciar a aplicação com o New Relic
CMD ["flask", "--app", "app", "run", "--debug", "--host", "0.0.0.0"]