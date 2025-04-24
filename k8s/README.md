# Deploy do CRM no Kubernetes via Minikube

## Pré-requisitos

- Minikube instalado e em execução
- Docker com as imagens `crm-backend` e `crm-frontend` construídas localmente

## Passos

1. Aplique os arquivos YAML:

   ```bash
   kubectl apply -f backend-deployment.yaml
   kubectl apply -f frontend-deployment.yaml
