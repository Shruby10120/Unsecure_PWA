# Import dependencies
import db_interface as db_manager
from flask import Flask
from flask import render_template
from flask import request

is_logged_in = False

# Create an instance of the Flask class in the app variable
app = Flask(__name__)


# Define the route for the index page at domain root
@app.route("/", methods=["POST", "GET"])
def index_page():
    global is_logged_in
    email = None
    if request.method == "POST":
        if request.form["password"].isdigit():
            password = int(request.form["password"])
            email = request.form["email"]
            is_logged_in = db_manager.check_login(email, password)
        app.logger.critical(f"{email} is logged in ? {is_logged_in}")
    return render_template("index.html", is_logged_in=is_logged_in, email=email), 200





# Initialize the Flask application
if __name__ == "__main__":
    app.run(debug=True)
