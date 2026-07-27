import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

# Initialize Flask App
app = Flask(__name__)

# Secret key required for flashing user feedback messages in Flask
app.config['SECRET_KEY'] = 'dev-secret-key-resume-analyzer-123'

# Configure upload target directory
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure allowed file extensions
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    """
    Helper function to check if the uploaded file has a permitted extension (.pdf).
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Handles both GET (rendering form) and POST (processing uploaded resume & job description).
    """
    if request.method == 'POST':
        # 1. Check if the file part exists in the request
        if 'resume_file' not in request.files:
            flash('No file part submitted in the form.', 'danger')
            return redirect(request.url)
            
        file = request.files['resume_file']
        job_description = request.form.get('job_description', '').strip()

        # 2. Check if user submitted an empty file input
        if file.filename == '':
            flash('No file selected. Please choose a PDF resume.', 'warning')
            return redirect(request.url)

        # 3. Validate file extension and process upload
        if file and allowed_file(file.filename):
            # Sanitize file name for OS safety
            filename = secure_filename(file.filename)
            
            # Ensure upload folder exists
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            
            # Build full file path and save
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            flash(f'Resume "{filename}" uploaded and saved successfully!', 'success')
            
            # Render index with confirmation (Temporary step before adding text parsing)
            return render_template(
                'index.html',
                uploaded_file=filename,
                job_desc=job_description
            )
        else:
            flash('Invalid file type! Please upload a .PDF document only.', 'danger')
            return redirect(request.url)

    # Standard GET request: render empty form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)