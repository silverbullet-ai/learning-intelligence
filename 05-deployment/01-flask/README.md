# Flask Framework

## Overview

Flask is a lightweight Python web framework used to build:

- Websites
- Web Applications
- REST APIs
- Machine Learning Deployment Applications
- Data Science Dashboards

Flask is widely used by Data Scientists, ML Engineers, and AI Engineers to deploy machine learning models through a web interface.

---

## Why Flask?

Machine learning models usually run as Python scripts.

Users cannot interact directly with those scripts.

Flask provides a web interface between users and models.

```text
User
  ↓
Web Interface
  ↓
Flask Application
  ↓
Machine Learning Model
  ↓
Prediction
```

---

## Popular Python Web Frameworks

| Framework | Description                       |
| --------- | --------------------------------- |
| Flask     | Lightweight and beginner-friendly |
| Django    | Full-stack framework              |
| FastAPI   | High-performance API framework    |
| Streamlit | Data Science and AI dashboards    |

---

## Core Components of Flask

### WSGI

WSGI stands for:

Web Server Gateway Interface

It acts as a bridge between:

```text
Web Server
     ↕
    WSGI
     ↕
Flask Application
```

Examples of web servers:

- Apache
- Nginx
- AWS
- Azure

---

### Jinja2 Template Engine

Jinja2 is Flask's default template engine.

It combines:

- HTML Templates
- Dynamic Data

to generate dynamic web pages.

Example:

```html
<h1>Hello {{ username }}</h1>
```

Output:

```html
Hello Aahish
```

or

```html
Hello Manav
```

depending on the supplied data.

---

## Installing Flask

requirements.txt

```text
flask
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Basic Project Structure

```text
flask-project/
│
├── app.py
├── requirements.txt
├── templates/
└── static/
```

---

## Creating a Flask Application

```python
from flask import Flask

app = Flask(__name__)
```

This creates the Flask application instance.

---

## Understanding __name__

When a file is executed directly:

```python
print(__name__)
```

Output:

```text
__main__
```

Flask uses `__name__` to locate:

- Project root
- Templates folder
- Static folder

---

## Creating Routes

A route maps a URL to a Python function.

Example:

```python
@app.route("/")
def home():
    return "Welcome to Flask"
```

URL Mapping:

```text
/  → home()
```

---

## Multiple Routes

```python
@app.route("/")
def home():
    return "Home Page"


@app.route("/about")
def about():
    return "About Page"


@app.route("/contact")
def contact():
    return "Contact Page"
```

---

## Running the Application

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Start the server:

```bash
python app.py
```

Output:

```text
* Running on http://127.0.0.1:5000
```

---

## Debug Mode

```python
app.run(debug=True)
```

Benefits:

- Automatic Reloading
- Better Error Messages
- Faster Development

---

## Request Flow

```text
Browser
   ↓
URL Request
   ↓
Route Matching
   ↓
Associated Function
   ↓
Response Returned
```

Example:

```text
/about
   ↓
about()
   ↓
"About Page"
```

---

## Common Beginner Mistakes

### Forgetting @app.route

Wrong:

```python
app.route("/")
def home():
    pass
```

Correct:

```python
@app.route("/")
def home():
    pass
```

---

### Duplicate Function Names

Each route function must have a unique name.

---

### Forgetting Flask Installation

```bash
pip install flask
```

---

## Key Takeaways

- Flask is lightweight and beginner-friendly.
- WSGI connects web servers and Flask applications.
- Jinja2 creates dynamic web pages.
- Routes map URLs to Python functions.
- Flask is widely used for ML and AI deployment.

# Flask Templates & Jinja2

## Overview

Flask provides the `render_template()` function to render HTML pages stored in the `templates` directory.

Instead of writing HTML directly inside Python code, Flask encourages separation of:

- Backend Logic (Python)
- Frontend Presentation (HTML)

This improves maintainability and follows modern web development practices.

---

## Returning HTML Directly

```python
@app.route("/")
def home():
    return """
    <html>
        <h1>Welcome to Flask</h1>
    </html>
    """
```

While valid, this approach becomes difficult to maintain for larger applications.

---

## Using render_template()

```python
from flask import Flask, render_template

@app.route("/index")
def index():
    return render_template("index.html")
```

Flask searches for HTML files inside the `templates/` directory.

---

## Templates Folder Structure

```text
project/
│
├── app.py
│
└── templates/
    ├── index.html
    ├── about.html
    └── contact.html
```

Important:

The folder name must be:

templates

Flask automatically searches this folder.

---

## Example Route Mapping

| URL      | Template     |
| -------- | ------------ |
| /index   | index.html   |
| /about   | about.html   |
| /contact | contact.html |

---

## Example HTML Page

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
</head>
<body>

<h1>Welcome to Flask</h1>

<p>This is the index page.</p>

</body>
</html>
```

---

## Jinja2 Template Engine

Flask uses Jinja2 as its default template engine.

Example:

Python:

```python
return render_template(
    "index.html",
    name="Aahish"
)
```

HTML:

```html
<h1>Hello {{ name }}</h1>
```

Output:

```text
Hello Aahish
```

Jinja2 allows:

- Variable Rendering
- Loops
- Conditions
- Dynamic Pages

---

## Common Errors

### TemplateNotFound

```python
return render_template("index.html")
```

but:

```text
templates/
└── index1.html
```

Error:

```text
TemplateNotFound: index.html
```

---

### Wrong Folder Name

Wrong:

```text
template/
```

Correct:

```text
templates/
```

---

## Why Templates?

Benefits:

- Cleaner Code
- Frontend/Backend Separation
- Easier Maintenance
- Better Collaboration

---

## Interview Questions

### What is render_template()?

> Used to render HTML files from the templates directory.

### Which template engine does Flask use?

> Jinja2

### Where should HTML files be stored?

> Inside the templates folder.

### What causes TemplateNotFound?

> Missing or incorrectly named template files.

---

## Key Takeaways

- Flask uses render_template() to serve HTML pages.
- HTML files belong inside the templates directory.
- Jinja2 powers dynamic web page rendering.
- Templates help separate frontend and backend code.

---

## HTTP Methods

HTTP methods define the action performed between a client and a server.

| Method | Purpose       |
| ------ | ------------- |
| GET    | Retrieve data |
| POST   | Send data     |
| PUT    | Update data   |
| DELETE | Delete data   |

In Flask, GET and POST are the most commonly used methods.

---

### GET Request

GET is used to retrieve information from a server.

Example:

```python
@app.route("/")
def home():
    return render_template("index.html")
```

Flask uses GET as the default method.

---

---

### POST Request

POST is used to send information from the client to the server.

Common examples:

- Login Forms
- Registration Forms
- Contact Forms
- Search Forms

---

### Handling Forms

Flask provides the request object for accessing incoming requests.

```python
from flask import request
```

---

## request Object

Common attributes:

- request.method
- request.form
- request.args
- request.files

Example:

```python
request.form["name"]
```

## Dynamic URL Routing

Flask supports dynamic URL parameters through **Variable Rules**.

Example:

```python
@app.route("/success/<score>")
def success(score):
    return f"Marks = {score}"
```

URL:

```
/success/85
```

Output:

```
Marks = 85
```

---

### Variable Converters

| Converter | Description    |
| --------- | -------------- |
| string    | Default string |
| int       | Integer        |
| float     | Decimal number |
| path      | File path      |
| uuid      | UUID value     |

Example:

```python
@app.route("/student/<int:id>")
```

---

## redirect()

The `redirect()` function sends the client to another route.

Example:

```python
return redirect("/success")
```

It is commonly used after processing forms.

---

## url_for()

`url_for()` generates URLs dynamically using route function names.

Example:

```python
url_for("success", score=85)
```

Generated URL:

```
/success/85
```

Benefits:

- No hardcoded URLs
- Easier maintenance
- Safer refactoring

---

## Jinja2 Template Engine

Jinja2 is Flask's default template engine.

It allows Python variables to be rendered inside HTML templates.

Example:

```python
return render_template(
    "result.html",
    name="Aahish"
)
```

HTML:

```html
<h1>Hello {{ name }}</h1>
```

---

## Jinja2 Syntax

### Expressions

```html
{{ variable }}
```

Used to display values.

---

### Control Statements

```html
{% if score >= 50 %}
{% endif %}
```

Supports:

- if
- elif
- else
- for

---

### Comments

```html
{# This comment is hidden #}
```

---

## Passing Data to Templates

Python:

```python
return render_template(
    "result.html",
    score=88
)
```

HTML:

```html
<h2>{{ score }}</h2>
```

## Jinja2 If Statement

```html
{% if score >= 50 %}
<h1>Pass</h1>
{% else %}
<h1>Fail</h1>
{% endif %}
```

## Jinja2 For Loop

Python:

```python
data = {
    "score": 80,
    "result": "Pass"
}
```

HTML:

```html
{% for key, value in data.items() %}
<h3>{{ key }}</h3>
<p>{{ value }}</p>
{% endfor %}
```

## Request Flow

```
Browser
   │
   ▼
HTML Form
   │
POST Request
   │
Flask Route
   │
Business Logic
   │
redirect(url_for(...))
   │
Jinja2 Template
   │
Response
```
