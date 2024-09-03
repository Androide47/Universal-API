from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Blog

blog_routes = Blueprint('blog_routes', __name__)


@blog_routes.route('/blogs', methods=['GET'])
def get_all_blogs():
    """Retrieve all blog posts."""
    blogs = Blog.query.all()
    blog_list = [blog.to_dict() for blog in blogs]
    return jsonify(blog_list)

@blog_routes.route('/blogs/<int:id>', methods=['GET'])
def get_blog(id):
    """Retrieve a single blog post by ID."""
    blog = Blog.query.get_or_404(id)
    return jsonify(blog.to_dict())

@blog_routes.route('/blogs', methods=['POST'])
def create_blog():
    """Create a new blog post."""
    data = request.get_json()
    new_blog = Blog(
        title=data['title'],
        content=data['content'],
        author=data.get('author', 'Anonymous')  # Default to 'Anonymous' if not provided
    )
    db.session.add(new_blog)
    db.session.commit()
    return jsonify(new_blog.to_dict()), 201

@blog_routes.route('/blogs/<int:id>', methods=['PUT'])
def update_blog(id):
    """Update an existing blog post by ID."""
    blog = Blog.query.get_or_404(id)
    data = request.get_json()
    blog.title = data.get('title', blog.title)
    blog.content = data.get('content', blog.content)
    blog.author = data.get('author', blog.author)
    db.session.commit()
    return jsonify(blog.to_dict())

@blog_routes.route('/blogs/<int:id>', methods=['DELETE'])
def delete_blog(id):
    """Delete a blog post by ID."""
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return jsonify({'message': 'Blog post deleted successfully.'})

