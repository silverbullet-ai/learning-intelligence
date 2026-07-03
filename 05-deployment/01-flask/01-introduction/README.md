
# Flask Introduction

## Overview

Flask is a lightweight Python web framework used to build:

- Websites
- Web Applications
- REST APIs
- Machine Learning Deployment Applications
- Data Science Dashboards

Flask is designed to be simple, flexible, and easy to learn. Unlike full-stack frameworks, it provides only the essential tools required to build web applications, allowing developers to choose additional libraries as needed.

---

# Why Flask?

As Data Scientists, Machine Learning Engineers, and AI Engineers, we often develop:

- Machine Learning Models
- Deep Learning Models
- NLP Applications
- Generative AI Applications

However, users cannot interact directly with Python scripts.

Instead, we need an interface:

```
User
   │
   ▼
Web Interface
   │
   ▼
ML Model
   │
   ▼
Prediction
```

Flask helps us build this web interface, making our AI and ML models accessible through a browser.

---

## Example

Suppose we build a Cat vs Dog Image Classification model.

The workflow becomes:

```
Upload Image
      │
      ▼
 Flask Application
      │
      ▼
 Machine Learning Model
      │
      ▼
 Prediction
      │
      ▼
 Display Result
```

Without Flask, the model exists only as a Python script.

With Flask, it becomes a complete web application.

---

# Popular Python Web Frameworks

| Framework | Description                       |
| --------- | --------------------------------- |
| Flask     | Lightweight and beginner-friendly |
| Django    | Full-stack web framework          |
| FastAPI   | High-performance API framework    |
| Streamlit | AI and Data Science dashboards    |

---

# Core Components of Flask

Two important concepts form the foundation of Flask:

- WSGI (Web Server Gateway Interface)
- Jinja2 Template Engine

---

# WSGI (Web Server Gateway Interface)

## What is WSGI?

WSGI stands for:

**Web Server Gateway Interface**

It is a communication standard between:

```
Web Server
      │
      ▼
    WSGI
      │
      ▼
Flask Application
```

---

## Why is WSGI Needed?

When a user visits a website, the request first reaches a web server.

Examples of web servers include:

- Apache
- Nginx
- AWS EC2
- Azure App Services
- Google Cloud

The web server cannot directly communicate with a Python application.

WSGI acts as the bridge between them.

---

## Architecture

```
User
 │
 ▼
Browser
 │
 ▼
Web Server
(Apache / Nginx)
 │
 ▼
WSGI
 │
 ▼
Flask Application
 │
 ▼
Response
 │
 ▼
Browser
```

---

## Request Flow

Example:

```
http://localhost:5000/
```

Flow:

```
Browser

↓

Web Server

↓

WSGI

↓

Flask Route

↓

Response

↓

Browser
```

---

# Jinja2 Template Engine

Jinja2 is Flask's default template engine.

It combines HTML templates with dynamic data to generate web pages.

Example:

Static HTML:

```html
<h1>Welcome User</h1>
```

Dynamic HTML:

```html
<h1>Welcome {{ username }}</h1>
```

Output:

```
Welcome Aahish
```

Jinja2 allows HTML pages to display dynamic content from Python.

---

# Installing Flask

Add Flask to your project:

```bash
pip install flask
```

Or include it in **requirements.txt**

```
flask
```

Then install:

```bash
pip install -r requirements.txt
```

---

# Basic Project Structure

```
flask-project/
│
├── app.py
├── requirements.txt
├── templates/
└── static/
```

Initially only these files are required:

```
flask-project/
│
├── app.py
└── requirements.txt
```

---

# Creating Your First Flask Application

Import Flask:

```python
from flask import Flask
```

Create the application:

```python
app = Flask(__name__)
```

This creates the Flask application object.

---

# Understanding `__name__`

`__name__` is a special Python variable.

If a file is executed directly:

```python
print(__name__)
```

Output:

```
__main__
```

If the file is imported:

```python
import app
```

Output:

```
app
```

Flask uses `__name__` to determine:

- Project root
- Template folder
- Static folder
- Resource locations

Therefore the standard syntax is:

```python
app = Flask(__name__)
```

---

# Creating Routes

A route maps a URL to a Python function.

Example:

```python
@app.route("/")
def home():
    return "Welcome to Flask"
```

Visiting:

```
http://localhost:5000/
```

calls:

```
home()
```

and returns:

```
Welcome to Flask
```

---

# Multiple Routes

Example:

```python
@app.route("/")
def home():
    return "Home"

@app.route("/about")
def about():
    return "About"

@app.route("/contact")
def contact():
    return "Contact"
```

URL Mapping

| URL      | Function  |
| -------- | --------- |
| /        | home()    |
| /about   | about()   |
| /contact | contact() |

---

# Understanding Decorators

Example:

```python
@app.route("/")
```

This decorator tells Flask:

Whenever this URL is requested, execute the function immediately below it.

---

# Running the Application

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Run:

```bash
python app.py
```

Output:

```
* Running on http://127.0.0.1:5000
```

Open:

```
http://localhost:5000
```

or

```
http://127.0.0.1:5000
```

---

# Understanding app.run()

Starts Flask's development server.

Examples:

Default:

```python
app.run()
```

Specify Host:

```python
app.run(host="127.0.0.1")
```

Specify Port:

```python
app.run(port=8080)
```

Enable Debug Mode:

```python
app.run(debug=True)
```

---

# Debug Mode

During development, use:

```python
app.run(debug=True)
```

Benefits:

- Automatic server reload
- Detailed error pages
- Faster development

Whenever the file is saved, Flask automatically restarts the server.

---

# Request Flow

```
Browser

↓

URL Request

↓

Route Matching

↓

Python Function

↓

Response

↓

Browser
```

---

# Common Beginner Mistakes

### Forgetting `@`

Incorrect:

```python
app.route("/")
```

Correct:

```python
@app.route("/")
```

---

### Duplicate Function Names

Each route must have a unique function.

Incorrect:

```python
@app.route("/")
def page():
    ...

@app.route("/about")
def page():
    ...
```

---

### Forgetting the Main Guard

Always use:

```python
if __name__ == "__main__":
    app.run()
```

---

### Flask Not Installed

Error:

```
ModuleNotFoundError: No module named 'flask'
```

Solution:

```bash
pip install flask
```

---

# Interview Questions

### What is Flask?

A lightweight Python web framework used to build web applications and REST APIs.

---

### What is WSGI?

Web Server Gateway Interface.

---

### Why is WSGI important?

It acts as the communication bridge between web servers and Python applications.

---

### What does `app = Flask(__name__)` do?

Creates the Flask application instance and initializes the WSGI application.

---

### What is a Route?

A route maps a URL to a Python function.

---

### What is the purpose of `@app.route()`?

It associates a URL with a specific Python function.

---

### Why do we use Debug Mode?

- Automatic server reload
- Better error messages
- Faster development

---

### What is the default Flask port?

```
5000
```

---

### What is localhost?

```
127.0.0.1
```

The loopback address that points to the current machine.

---

# Key Takeaways

- Flask is a lightweight Python web framework.
- Flask is widely used for AI, ML, and backend development.
- WSGI connects web servers with Flask applications.
- Jinja2 is Flask's template engine.
- `app = Flask(__name__)` creates the Flask application.
- Routes map URLs to Python functions.
- `app.run()` starts the development server.
- `debug=True` enables automatic reloading during development.
- Flask applications begin with a simple project structure and can be extended as projects grow.

