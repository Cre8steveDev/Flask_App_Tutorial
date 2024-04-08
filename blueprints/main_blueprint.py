from flask import Blueprint, request, render_template

main_views = Blueprint("main", __name__)

# Create routes on this blueprint instance
@main_views.get("/", strict_slashes=False)
def index():
    # Define application logic for homepage
    return render_template("index.html")


@main_views.get("/profile", strict_slashes=False)
def profile(username):
    # Define application logic for profile page
    return render_template("profile.html", username=username)
