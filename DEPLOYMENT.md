# Production Deployment Guide

This guide steps through how to deploy the Crafts by Cates website to a production environment.

## 1. Production Readiness Changes
We have updated the application to use industry-standard tools for production:
- **WSGI Server**: `gunicorn` replaces the default Flask development server for handling concurrent requests.
- **Security**: `flask-talisman` adds security headers (HSTS, CSP) to protect users.
- **Static Files**: `whitenoise` serves images and CSS efficiently without needing complex Nginx configuration.
- **Configuration**: `config.py` now enforces secure settings (HTTPS cookies, hidden debug mode) in production.

## 2. Environment Variables
In a production environment, you **must** set the following environment variables. Do not commit these to GitHub.

| Variable | Value | Description |
|----------|-------|-------------|
| `FLASK_ENV` | `production` | Tells Flask to use the `ProductionConfig` settings. |
| `SECRET_KEY` | (A long random string) | Used for cryptographic signing. Run `python -c 'import secrets; print(secrets.token_hex(32))'` to generate one. |
| `PORT` | `8000` (or assigned by host) | The port the server listens on. |

## 3. Testing Production Build Locally
Before deploying, test the production setup on your machine:

1. **Install Production Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables** (Linux/Mac):
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=test-key-123
   ```

3. **Run with Gunicorn**:
   ```bash
   gunicorn run:app --timeout 120
   ```
   
4. Visit `http://127.0.0.1:8000`. The site should load, and you should see secure headers in the Network tab of your browser dev tools.

## 4. Deployment Options

### Option A: Render / Heroku (PaaS) - Recommended
This project includes a `Procfile` which makes it ready for Platform-as-a-Service providers.

1. **Push to GitHub**: Ensure your latest code is committed and pushed.
2. **Create New Web Service**: Connect your repository.
3. **Environment Variables**: Add `FLASK_ENV` and `SECRET_KEY` in the provider's dashboard.
4. **Deploy**: The platform will detect `requirements.txt` and the `Procfile` automatically.

### Option B: DigitalOcean / VPS
If deploying to a VPS:

1. Clone the repo.
2. Set up a virtual environment and install requirements.
3. specific `gunicorn` systemd service:
   ```ini
   [Unit]
   Description=Gunicorn instance to serve cates-crafts
   After=network.target

   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/var/www/cates
   Environment="PATH=/var/www/cates/venv/bin"
   Environment="FLASK_ENV=production"
   Environment="SECRET_KEY=your-secret-key"
   ExecStart=/var/www/cates/venv/bin/gunicorn --workers 3 --bind unix:cates.sock -m 007 run:app

   [Install]
   WantedBy=multi-user.target
   ```
4. Configure Nginx to proxy requests to the socket.

## 5. Security Notes
- **Content Security Policy (CSP)**: We have configured a CSP that allows the Tailwind CDN. If you change to a local build of Tailwind, update the `csp` dictionary in `app/__init__.py`.
- **HTTPS**: The app enforces HTTPS. On a VPS, ensure you have an SSL certificate (e.g., via Let's Encrypt) on your reverse proxy (Nginx). On Render/Heroku, this is handled automatically.

