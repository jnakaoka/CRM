# backend/Dockerfile
FROM python:3.12

# Instala bibliotecas do sistema necessárias para o mysqlclient
RUN apt-get update \
  && apt-get install -y default-libmysqlclient-dev default-mysql-client build-essential \
  && apt-get clean

# Cria diretório da aplicação
WORKDIR /app

# Copia os arquivos e instala dependências do projeto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação
COPY . .

COPY wait-for-mysql.sh /wait-for-mysql.sh
RUN chmod +x wait-for-mysql.sh
ENTRYPOINT ["/wait-for-mysql.sh"]

# Roda o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
