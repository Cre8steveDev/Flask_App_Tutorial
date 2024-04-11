from flask import Blueprint, request, render_template, send_from_directory

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


@main_views.get("/download/<string:filename>", strict_slashes=False)
def download(filename):
    # Using the send_from_directory function you can send a file
    # By providing the absolute path to the file
    # Note the /tmp/ is just for practice purpose.
    # You decide which directory you want to store your files at
    return send_from_directory(f"/tmp/Tutorial/{filename}")
