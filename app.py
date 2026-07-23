# Import the Flask class from the flask package
from flask import Flask

# Initialize the Flask application
# __name__ is a special built-in Python variable that tells Flask 
# where to look for resources like templates and static files.
app = Flask(__name__)

# Define a route for the homepage
# The decorator @app.route('/') maps the root URL ("/") to this function
@app.route('/')
def home():
    """
    Function that handles requests to the root URL ("/").
    Returns a simple welcoming text response to the client's browser.
    """
    return "AI Resume Analyzer Backend is Running Successfully!"

# Check if this script is executed directly (not imported as a module in another script)
if __name__ == '__main__':
    # Run the Flask local development server
    # debug=True enables live code reloading and detailed error messages in the browser
    app.run(debug=True, port=5000)