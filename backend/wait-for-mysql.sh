#!/bin/bash
echo "Esperando o MySQL ficar disponível..."

echo "Verificando conexão com o MySQL: host=$MYSQL_HOST, user=$MYSQL_USER, password=$MYSQL_PASSWORD"

until mysql -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e 'SELECT 1'; do
  >&2 echo "MySQL ainda não está pronto - esperando"
  sleep 2
done

echo "MySQL está pronto - iniciando o Django"
exec "$@"
