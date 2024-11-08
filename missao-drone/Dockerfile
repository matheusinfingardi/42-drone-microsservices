# Dockerfile

# Usar a imagem oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY ./src /app

# Expor a porta para a aplicação
EXPOSE 8000

# Iniciar a aplicação com Uvicorn
CMD ["uvicorn", "src/interfaces/api:app", "--host", "0.0.0.0", "--port", "8000"]
