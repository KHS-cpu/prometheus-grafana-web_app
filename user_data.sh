#!/bin/bash

# Update and install Docker + Docker Compose
apt update -y
apt install -y docker.io docker-compose

# Add the 'ubuntu' user to the docker group
usermod -aG docker ubuntu

# Enable and start Docker
systemctl enable docker
systemctl start docker