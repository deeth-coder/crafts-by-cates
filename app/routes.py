import os
import json
from flask import Blueprint, render_template, current_app, request, jsonify
from app.services import add_email_to_sheet


# Define the main blueprint for our routes
bp = Blueprint('main', __name__)

def load_json(filename):
    """
    Helper function to load content from JSON files in the app/content directory.
    This allows for easy content updates without changing Python code.
    """
    path = os.path.join(current_app.root_path, 'content', filename)
    with open(path, 'r') as f:
        return json.load(f)

@bp.app_errorhandler(404)
def page_not_found(e):
    """Global 404 error handler."""
    copy = load_json('copy.json')
    return render_template('404.html', copy=copy), 404

@bp.route('/')
def home():
    """
    Home Page Route
    Loads content for Hero, About, Featured Projects, and recent Blog posts.
    To update homepage text, edit app/content/copy.json.
    """
    copy = load_json('copy.json')
    projects = load_json('projects.json')
    blog_posts = load_json('blog.json')
    
    # Filter top 3 projects and posts for home page display
    featured_projects = projects[:3]
    recent_posts = blog_posts[:3]
    
    return render_template('home.html', copy=copy, projects=featured_projects, posts=recent_posts)

@bp.route('/projects')
def projects():
    """
    Portfolio Page Route
    Lists all projects from app/content/projects.json.
    To add a new project, simply add an entry to that JSON file.
    """
    copy = load_json('copy.json')
    projects = load_json('projects.json')
    return render_template('projects.html', copy=copy, projects=projects)

@bp.route('/projects/<id>')
def project_detail(id):
    """
    Individual Project Route
    Displays details, gallery, and 'behind the scenes' content for a project.
    """
    copy = load_json('copy.json')
    projects = load_json('projects.json')
    
    # Find project by ID
    project = next((p for p in projects if p['id'] == id), None)
    
    if not project:
        return render_template('404.html', copy=copy), 404
        
    return render_template('project_detail.html', copy=copy, project=project)

@bp.route('/blog')
def blog_index():
    """
    Blog Index Route
    Lists all blog posts from app/content/blog.json.
    To add a new post, add an entry to the JSON file.
    """
    copy = load_json('copy.json')
    posts = load_json('blog.json')
    return render_template('blog_index.html', copy=copy, posts=posts)

@bp.route('/blog/<slug>')
def blog_post(slug):
    """
    Individual Blog Post Route
    Finds a post by its 'slug' field in app/content/blog.json.
    """
    copy = load_json('copy.json')
    posts = load_json('blog.json')
    # Search for the post with the matching slug
    post = next((p for p in posts if p['slug'] == slug), None)
    
    if not post:
        return render_template('404.html', copy=copy), 404
        
    return render_template('blog_post.html', copy=copy, post=post)

@bp.route('/join-maker-list', methods=['POST'])
def join_maker_list():
    """
    API Endpoint to join the maker list.
    Expects JSON: { "email": "user@example.com" }
    """
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
        
    # Basic email validation could go here
    
    success = add_email_to_sheet(email)
    
    if success:
        return jsonify({'message': 'Successfully joined the list!'}), 200
    else:
        return jsonify({'error': 'Failed to join list. Please try again later.'}), 500
