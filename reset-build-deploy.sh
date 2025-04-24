#!/bin/bash

echo "🟡 Verificando o status do Minikube..."
if ! minikube status &>/dev/null; then
    echo "🚀 Iniciando o Minikube..."
    minikube start || { echo "❌ Erro ao iniciar o Minikube"; exit 1; }
else
    echo "✅ Minikube já está rodando."
fi

echo "🔧 Configurando ambiente Docker para usar o Minikube..."
eval $(minikube docker-env)

# Build da imagem do backend
echo "🏗️  Buildando imagem Docker: crm-backend:latest..."
docker build -t crm-backend:latest -f ./backend/Dockerfile ./backend || {
    echo "❌ Erro ao criar a imagem Docker do backend. Verifique o Dockerfile."
    exit 1
}

# Build da imagem do frontend
echo "🏗️  Buildando imagem Docker: crm-frontend:latest..."
docker build -t crm-frontend:latest -f ./frontend/Dockerfile ./frontend || {
    echo "❌ Erro ao criar a imagem Docker do frontend. Verifique o Dockerfile."
    exit 1
}

echo "🧹 Limpando recursos antigos do Kubernetes..."
kubectl delete -f k8s/frontend-deployment.yaml --ignore-not-found
kubectl delete -f k8s/backend-deployment.yaml --ignore-not-found

echo "🚀 Aplicando novos manifests do Kubernetes..."
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-deployment.yaml

echo "✅ Build e deploy concluídos com sucesso!"

echo "🔍 Verificando pods e serviços:"
kubectl get pods
kubectl get services