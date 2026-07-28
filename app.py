import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

# Import our custom PDF extraction utility module
from utils.pdf_parser import extract_text_from_pdf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-resume-analyzer-123'

# Upload folder configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'resume_file' not in request.files:
            flash('No file part submitted in the form.', 'danger')
            return redirect(request.url)
            
        file = request.files['resume_file']
        job_description = request.form.get('job_description', '').strip()

        if file.filename == '':
            flash('No file selected. Please choose a PDF resume.', 'warning')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Step 6 Integration: Extract text from the saved PDF resume
            extracted_text = extract_text_from_pdf(file_path)

            if not extracted_text:
                flash('Could not extract text from the PDF. It may be an image-only or scanned PDF.', 'warning')
                return redirect(request.url)

            # Calculate text stats
            word_count = len(extracted_text.split())
            char_count = len(extracted_text)

            flash(f'Resume "{filename}" processed successfully!', 'success')

            return render_template(
                'index.html',
                uploaded_file=filename,
                job_desc=job_description,
                extracted_text=extracted_text,
                word_count=word_count,
                char_count=char_count
            )
        else:
            flash('Invalid file type! Please upload a .PDF document only.', 'danger')
            return redirect(request.url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)