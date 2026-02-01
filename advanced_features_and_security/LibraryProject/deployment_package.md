# Deployment Configuration - HTTPS and SSL Setup

To ensure the Django application is served securely in a production environment, an Nginx reverse proxy is used to handle SSL termination.

## Nginx Configuration Example
The following configuration should be placed in your Nginx sites-available directory (e.g., `/etc/nginx/sites-available/library_project`):

```nginx
# Redirect all HTTP traffic to HTTPS
server {
    listen 80;
    server_name yourdomain.com; # Replace with your actual domain
    return 301 https://$host$request_uri;
}

# Handle HTTPS traffic
server {
    listen 443 ssl;
    server_name yourdomain.com;

    # SSL Certificate paths (typically provided by Let's Encrypt/Certbot)
    ssl_certificate /etc/letsencrypt/live/[yourdomain.com/fullchain.pem](https://yourdomain.com/fullchain.pem);
    ssl_certificate_key /etc/letsencrypt/live/[yourdomain.com/privkey.pem](https://yourdomain.com/privkey.pem);

    # Optimization for security
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        proxy_pass [http://127.0.0.1:8000](http://127.0.0.1:8000);
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # This header is essential for Django's SECURE_SSL_REDIRECT to work!
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}