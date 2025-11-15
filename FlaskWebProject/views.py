"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect, request, session, url_for
from werkzeug.urls import url_parse
from config import Config
from . import app, db
from .forms import LoginForm, PostForm
from flask_login import current_user, login_user, logout_user, login_required
from .models import User, Post
import msal
import uuid

# Blob storage URL
imageSourceUrl = f'https://{app.config["BLOB_ACCOUNT"]}.blob.core.windows.net/{app.config["BLOB_CONTAINER"]}/'


@app.route('/')
@app.route('/home')
@login_required
def home():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    posts = Post.query.all()
    return render_template('index.html', title='Home Page', posts=posts)


@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = Post()
        post.save_changes(form, request.files['image_path'], current_user.id, new=True)
        return redirect(url_for('h_
