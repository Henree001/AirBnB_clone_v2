#!/usr/bin/env bash
# Installs, configures, and starts the web server
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "My new website" | sudo tee /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "15i\    location /hbnb_static/ {\n\talias /data/web_static/current/;\n\    }" /etc/nginx/sites-available/default
sudo service nginx restart
