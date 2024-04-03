#i/bin/bash

#confirm that Nginx installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

#creat the neccessary folders if not created
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

#creat a fake html file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_block="location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html;
}"
sudo sed -i "/server_name _;/a $config_block" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
