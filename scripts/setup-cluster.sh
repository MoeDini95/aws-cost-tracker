#!/bin/bash

set -e

echo "Creating KIND Cluster..."

kind create cluster --name aws-cost-tracker

echo "Installing the Nginx Controller..."

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

echo "Waiting for ingress controller to be ready..."

kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s

echo "Cluster is ready!..."