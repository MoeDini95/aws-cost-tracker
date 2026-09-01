#!/bin/bash
set -e

echo "Starting terraform deployment on AWS..."

cd "$(dirname "$0")/../infrastructure/terraform"

echo "Initializing Terraform..."

terraform init

echo "Formatting terraform code.."

terraform fmt

echo "Validating terraform code for errors..."

terraform validate

echo "Running terraform plan..."

terraform plan

echo "Applying terraform infrastructure onto AWS..."

terraform apply -auto-approve #auto approve without yes prompt

echo "Infrastructure deployed!..."