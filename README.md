# Crafts by Cates

A cozy, mobile-first personal website for a crochet/knitting/sewing brand, built with Flask and Tailwind CSS.

## Project Overview

This website showcases a portfolio of handmade fiber arts projects, a blog for tutorials and updates, and an email signup for community building. It is designed with a "warm neutral" aesthetic using Tailwind CSS.

**Key Features:**
- **Mobile-First Design:** Responsive layout that looks great on phones and desktops.
- **Dynamic Content:** Blog posts and projects are loaded from JSON files, making updates easy without touching HTML/Python code.
- **Cozy Aesthetic:** Custom color palette configured in Tailwind.
- **Performance Optimized:** Automatic image resizing and WebP conversion for fast loading speeds.

## Local Development

### Prerequisites
- Python 3.8+
- `pip` (Python package manager)

### Setup
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd crafts_by_cates
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   # For development (auto-reload, debug logs)
   python run.py
   
   # OR for production simulation
   gunicorn run:app --timeout 120
   ```

5. **View the site:**
   Open your browser and navigate to `http://127.0.0.1:5000` (Flask) or `http://127.0.0.1:8000` (Gunicorn).

## Content Management

The content is separated from the code to make updates simple. All content files are located in `app/content/`.

For a detailed guide on adding projects and blog posts, see **[PROJECT_CONTENT_GUIDE.md](PROJECT_CONTENT_GUIDE.md)**.

### Updating Text (Hero, About, Footer, etc.)
Edit `app/content/copy.json`. This file contains the text for the homepage hero section, about me, join community, future offerings, and footer links.

### Adding Images & Optimization
1. Save your high-res images in `app/static/img/`.
2. Run the optimization script to resize and compress them:
   ```bash
   python scripts/optimize_images.py
   ```
   *This converts images to WebP and ensures they are web-friendly sizes.*

## Deployment

This application is ready to be deployed on Platform-as-a-Service (PaaS) providers like Render or Railway.

See **[DEPLOYMENT.md](DEPLOYMENT.md)** for full production deployment instructions.

### Quick Deploy (Render/Heroku)
The project includes a `Procfile` configured with the necessary timeouts for production.

1. **Push your code to GitHub.**
2. **Connect repository** to your host.
3. **Environment Variables:** Set `FLASK_ENV=production` and `SECRET_KEY` (random string).
4. **Deploy.**

## Customization

### Styles (Tailwind CSS)
The site uses Tailwind CSS via a CDN script in `app/templates/base.html` for easy development. 
- The configuration (colors, fonts) is defined in the `<script>` tag in `base.html`.
- To change the color palette, edit the `colors` object in the `tailwind.config`.

## Future Improvements

- **Database:** Migrate from JSON files to a SQLite/PostgreSQL database for better scalability.
- **Markdown Support:** Implement a Markdown parser for richer blog post formatting.
- **Contact Form:** Connect the email signup form to a service like Mailchimp or a simple email backend (e.g., Flask-Mail).
