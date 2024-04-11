from flask import Blueprint, request, render_template, redirect
from flask_login import login_required, logout_user, current_user, login_user, flash
from werkzeug.security import generate_password_hash, check_password_hash

auth_views = Blueprint("auth", __name__)

# Create routes on this blueprint instance
@auth_views.route("/register", strict_slashes=False, methods=["GET", "POST"])
def register():
    # Define application logic for homepage
    if request.method == "POST":
        uploaded_file = request.files['picture']
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        
        # Save the uploaded file to a directory on your server
        # Preferably in a folder you define in your app directory
        # example in static/profile_pic/
        uploaded_file.save(f"/static/profile_pic/{uploaded_file.filename}")
        
        # Implement database logic to register user
        # Create a dictionary of your user details to insert into the MongoDB Collection for a new User 
        new_user = {
            "username": username,
            "email": email,
            "password": generate_password_hash(password),
            "profile_pic": f"/static/profile_pic/{uploaded_file.filename}"
        }
        try:
            # Retrieve the usercollection from database
            from models.database import user
            
            # Check if the email/username already exists in db
            check_email = user.find_one({"email": request.form.get("email")})
            check_username = user.find_one({"username": request.form.get("username")})
        
            if check_email or check_username:
                flash("Credentials Already in use!", "error")
                return redirect("/register")
        
            new_user = user.insert_one(new_user)
            return redirect("/login")
        
        # If any error occurs, we can catch it
        except Exception as e:
            print(e)
            flash("Error occured during registration. Try again!", "error")
            return redirect("/register"),

    # When it's a GET request we sent the html form
    return render_template("register.html")


@auth_views.route("/login", strict_slashes=False, methods=["GET", "POST"])
def login():
    # Define application logic for profile page
    # If a user alredy exists and tries to be funny by
    # manually entering the /login route, they should be 
    # redirected to the index page 
    if current_user.is_authenticated:
        return redirect("/")
    
    if request.method == "POST":
        # Enter logic for processing registration
        from models.database import user, User
        
        # Get username and password from the form
        username = request.form.get("username")
        user_password = request.form.get("password")
        
        # Retrieve user from the database with username
        find_user = user.find_one({"username": username})
        
        # Return an error if user not in database
        if find_user == None:
            flash("Invalid Login Credentials!", "error")
            return redirect("/login")

        # Compare the user's password with the password returned from db
        
        is_valid_password = check_password_hash(find_user.get("password"), user_password)
        
        # If password does not match, redirect user to login again
        if not is_valid_password:
            flash("Invalid Login Credentials!", "error")
            return redirect("/login")
            
        # At this point all is well; so instantiate the User class 
        # This is to enable the Flask-Login Extension kick in
        log_user = User(find_user.get("username"), str(find_user.get("_id")))
        
        # use the login_user function imported from flask_login
        login_user(log_user)

        # Then return the user to the index page after sucess
        return redirect("/")
    
        # Make sure to do proper error handling with try/except
        # I don't want to make the code too bulky
    
    # for Get request to the route, we sent the html form
    return render_template("login.html")


# Create Sign Out Route 
@auth_views.route("/logout", strict_slashes=False)
@login_required
def logout():
    # We wrap the logout function with @login_required decorator
    # So that only logged in users should be able to 'log out'
    logout_user()
    return redirect("/")

