from flask import Blueprint, request, render_template
from flask import redirect

auth_views = Blueprint("auth", __name__)

# Create routes on this blueprint instance
@auth_views.route("/register", strict_slashes=False, methods=["GET", "POST"])
def register():
    # Define application logic for homepage
    if request.method == "POST":
        # Enter logic for processing registration
        return render_template("login.html")
    
    return render_template("register.html")


@auth_views.route("/login", strict_slashes=False, methods=["GET", "POST"])
def login():
    # Define application logic for profile page
    if request.method == "POST":
        # Enter logic for processing registration
        return redirect("/profile")
    
    return render_template("login.html")
