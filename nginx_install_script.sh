#!/bin/bash

# Install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Check if Nginx is running
nginx_status=$(sudo systemctl is-active nginx)

if [ "$nginx_status" = "active" ]; then
    echo "Nginx is running."
else
    echo "Nginx is not running. Starting Nginx..."
    sudo systemctl start nginx
    echo "Nginx started successfully."
fi

# Read Nginx configuration
echo "Reading Nginx configuration:"
nginx_config=$(cat /etc/nginx/nginx.conf)
echo "$nginx_config"

