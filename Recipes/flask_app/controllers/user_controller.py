from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import user
from datetime import datetime
dateFormat = "%m/%d/%Y %I:%M %p"

@app.route('/recipes')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html', 
        current_user = user.User.getById({'id': session['user_id']}),
        all_users = user.User.get_all(),
        dtf = dateFormat)
    return redirect('/')

