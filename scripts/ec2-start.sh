#!/usr/bin/env bash

set -e
INSTANCE_ID="i-0f6a7d02ec78aea52"

echo "Starting EC2 instance..."

aws ec2 start-instances --instance-ids $INSTANCE_ID --region us-east-1

echo "Waiting for instance to run..."

aws ec2 wait instance-running --instance-ids $INSTANCE_ID --region us-east-1

echo "Fetching new public IP..."

aws ec2 describe-instances \
  --instance-ids $INSTANCE_ID \
  --query 'Reservations[0].Instances[0].PublicIpAddress' \
  --output text \
  --region us-east-1

echo "EC2 instance is running..."