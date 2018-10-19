from app import app, db, followers
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'followers':followers, 'User': User, 'Post': Post}