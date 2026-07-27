# NOTES (macOS)

## Requirements

* macOS
* Python 3.10 or later

Check your Python version:

```bash
python3 --version
```

## Create a Virtual Environment

```bash
python3 -m venv venv
```

## Activate the Virtual Environment

```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your Terminal prompt.

## Install the Required Packages

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install Flask manually:

```bash
pip install flask
```

## Run the Application

```bash
python app.py
```

or

```bash
python3 app.py
```

If the application starts successfully, you should see output similar to:

```
 * Running on http://127.0.0.1:5000
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Stop the Application

Press:

```
Ctrl + C
```

## Deactivate the Virtual Environment

When you're finished:

```bash
deactivate
```

## Troubleshooting

If you see:

```
ModuleNotFoundError: No module named 'flask'
```

Install Flask:

```bash
pip install flask
```

If another package is missing, install it using:

```bash
pip install <package_name>
```

Then run the application again.
