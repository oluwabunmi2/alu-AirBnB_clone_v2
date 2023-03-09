#!/usr/bin/env bash
# automatically installing nginx server and creating folders 

sudo apt-get update
sudo apt-get -y install nginx 
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/shared/
sudo sh -c 'echo "This is a message to test the nginx configuration" >> /data/web_static/releases/test/index.html'
sudo -s /data/web_static/current /data/web_static/releases/test/
sudo chown -hR ubuntu /data/
sudo service nginx restart
