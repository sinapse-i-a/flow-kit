# Imagem base com suporte ao CUDA
FROM nvidia/cuda:11.8.0-base-ubuntu22.04

# Instale dependências do sistema
RUN apt-get update && apt-get install -y \
    python3 python3-pip git wget ffmpeg libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Configure Python como python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Configure o diretório de trabalho
WORKDIR /usr/src/app

# Copie o arquivo requirements.txt para instalar as dependências
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos da aplicação
COPY ./app /usr/src/app

# Comando padrão para rodar o script principal
CMD ["python", "image-processing.py"]
