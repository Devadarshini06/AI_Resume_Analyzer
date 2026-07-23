# Import Flask and render_template function
from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Route for the Home Page
@app.route('/')
def home():
    """
    Renders the homepage template (index.html) and passes
    dynamic Python context data into the Jinja2 engine.
    """
    # Dynamic data we want to pass into HTML
    title = "AI Resume Analyzer"
    status = "Active & Ready"
    project_features = [
        "PDF Resume Text Extraction",
        "Contact Information Extraction (Email, Phone, Links)",
        "Automated Skill Matching & ATS Scoring",
        "Google Gemini AI Insights & Suggestions",
        "Downloadable PDF Analysis Reports"
    ]
    
    # render_template searches in the 'templates/' folder
    # We pass data as key=value arguments
    return render_template(
        'index.html', 
        project_title=title, 
        app_status=status, 
        features=project_features
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)