#!/usr/bin/env bash

set -e

INSTANCE_ID="i-0f6a7d02ec78aea52"

echo "Stopping EC2 instance..."

aws ec2 stop-instances --instance-ids $INSTANCE_ID --region us-east-1

echo "Waiting for instance to stop..."

aws ec2 wait instance-stopped --instance-ids $INSTANCE_ID --region us-east-1

echo "EC2 instance has stopped..."