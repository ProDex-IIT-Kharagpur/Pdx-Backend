from flask import Flask, render_template, request, redirect, url_for, flash, abort
from website import app,db
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import login_user, login_required, logout_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog_posts():
    return render_template('blog.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
