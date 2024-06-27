# 0x1A. Application server
![alt text](image.png)


## Overview

* In this project, I enhanced the web infrastructure by integrating a Gunicorn application server with web-01. I manually configured Gunicorn to bind to different ports to serve a Flask application and set up Nginx to proxy pass requests to Gunicorn. Additionally, I created a gunicorn.service file in the `` /etc/systemd/system `` directory to ensure the Gunicorn service starts automatically on boot. Finally, I developed a bash script to update the application server seamlessly, ensuring zero downtime during updates.

## Background Context

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.
