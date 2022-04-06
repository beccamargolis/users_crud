from sqlite3 import connect
from flask import render_template, redirect, request
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User

@app.route('/') # for home page, display all users from database
def index():
    users = User.get_all()
    return render_template("index.html", all_users = users) # we reference "all_users" in the Jinja in the html, so we have to specify what that means here

@app.route('/user/new') # to show the create user page
def new():
    return render_template("create_user.html")

@app.route('/create/user', methods=['POST']) # to actually create a new user and redirect back to home; POST method because data is being submitted
def create_user():
    User.save(request.form)
    return redirect('/')

@app.route('/user/show/<int:id>') # to render the "show" template to display user info
def show_user(id):
    one_user=User.get_one(id)
    return render_template("show_user.html", user=one_user)

@app.route('/user/edit/<int:id>') # to render the "edit" template to bring up editable, pre-populated fields
def edit_user(id):
    one_user=User.get_one(id)
    return render_template("edit_user.html", user=one_user)

@app.route('/user/update/<int:id>',methods=['POST']) # to actually edit a user and redirect back to home; POST method because data is being submitted
def update(id):
    User.update(request.form, id)
    return redirect('/')

@app.route('/user/delete/<int:id>') # delete user and redirect back to home
def destroy(id):
    User.destroy(id)
    return redirect('/')