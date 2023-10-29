# Use a imagem Alpine do Python como base
FROM python:3.8-alpine

# Crie o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt /app/

# Instale as dependências a partir do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do projeto para o contêiner
COPY . /app/

# Expõe a porta que a aplicação estará escutando (ajuste conforme necessário)
EXPOSE 5000

# Comando para iniciar a aplicação (substitua main.py pelo seu arquivo principal)
CMD ["python", "main.py"]
