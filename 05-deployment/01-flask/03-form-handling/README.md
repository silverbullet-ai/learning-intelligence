# Flask Form Handling

## Overview

Web applications become interactive when users can submit information to the server.

Flask provides built-in support for handling user input through HTML forms using HTTP requests.

In this section, you'll learn how forms work, understand HTTP methods, process user input, and retrieve submitted data using Flask's `request` object.

---

# What are HTTP Methods?

HTTP Methods (also known as **HTTP Verbs**) define the type of action a client wants to perform on a server.

Common HTTP methods include:

| Method | Purpose |
|----------|----------|
| GET | Retrieve data |
| POST | Send data |
| PUT | Update existing data |
| DELETE | Delete data |

In this module, we'll focus on the two most commonly used methods:

- GET
- POST

---

# GET Request

A **GET request** is used to retrieve information from the server.

Examples:

- Opening a webpage
- Reading information
- Loading images
- Viewing a dashboard

Example URL:

```
https://www.google.com
```

Workflow:

```
Browser

↓

GET Request

↓

Flask Server

↓

HTML Response

↓

Browser
```

No user data is submitted.

---

# Flask GET Example

```python
@app.route("/index")
def index():
    return render_template("index.html")
```

This is equivalent to:

```python
@app.route("/index", methods=["GET"])
```

because Flask uses **GET** as the default HTTP method.

---

# POST Request

A **POST request** is used whenever the client sends data to the server.

Examples:

- Login forms
- Registration forms
- Search forms
- Contact forms
- Feedback forms

Workflow:

```
User Input

↓

POST Request

↓

Flask

↓

Process Data

↓

Response
```

Unlike GET, POST carries user-submitted data.

---

# GET vs POST

| Feature | GET | POST |
|----------|-----|------|
| Purpose | Retrieve data | Send data |
| Sends user data | No | Yes |
| Used for | Viewing pages | Form submission |
| Default in Flask | Yes | No |

---

# The request Object

To access incoming HTTP requests, Flask provides the **request** object.

Import it using:

```python
from flask import Flask, render_template, request
```

The `request` object provides access to:

- HTTP method
- Form data
- URL parameters
- Uploaded files
- Cookies
- Headers

In this module, we'll use:

- `request.method`
- `request.form`

---

# Supporting Multiple HTTP Methods

A route can handle multiple request types.

Example:

```python
@app.route("/form", methods=["GET", "POST"])
def form():
    pass
```

This allows both:

- GET requests
- POST requests

to be handled by the same route.

---

# Why Use Both GET and POST?

When a user first visits a page:

```
http://localhost:5000/form
```

Flask receives a:

```
GET Request
```

and displays the form.

After the user submits the form:

```
POST Request
```

is sent to the same route.

Workflow:

```
Visit Page

↓

GET

↓

Display Form

↓

User Enters Data

↓

Submit

↓

POST

↓

Process Data

↓

Response
```

---

# Handling Request Methods

Example:

```python
@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "POST":
        pass

    return render_template("form.html")
```

GET Request:

```
Display HTML Form
```

POST Request:

```
Read Submitted Data

↓

Process

↓

Return Response
```

---

# Creating an HTML Form

Example:

```html
<form method="POST">

    <label>Name:</label>

    <input
        type="text"
        name="name"
    >

    <input
        type="submit"
        value="Submit"
    >

</form>
```

---

# Understanding the method Attribute

The form specifies:

```html
<form method="POST">
```

When the user clicks **Submit**, the browser sends a POST request to the server.

---

# Understanding the name Attribute

Example:

```html
<input
    type="text"
    name="name"
>
```

The **name** attribute identifies the field.

Flask retrieves its value using:

```python
request.form["name"]
```

Without a `name` attribute, Flask cannot access the submitted value.

---

# Retrieving Form Data

Example:

```python
@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        name = request.form["name"]

        return f"Hello {name}"

    return render_template("form.html")
```

If the user enters:

```
Aahish
```

Output:

```
Hello Aahish
```

---

# Complete Example

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "POST":

        name = request.form["name"]

        return f"Hello {name}"

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
```

---

# Request Flow

```
User opens

/form

↓

GET Request

↓

Display Form

↓

User fills form

↓

Submit

↓

POST Request

↓

request.form

↓

Process Data

↓

Return Response
```

---

# Why Forms are Important

Forms allow users to submit information such as:

- Name
- Email
- Password
- Search Queries
- Feedback
- Registration Details
- Login Credentials

Almost every modern web application relies on forms.

---

# Common Beginner Mistakes

## Forgetting POST Method

Incorrect:

```python
@app.route("/form")
```

or

```python
@app.route("/form", methods=["GET"])
```

Submitting the form results in:

```
Method Not Allowed
```

Correct:

```python
@app.route("/form", methods=["GET", "POST"])
```

---

## Using request.method Instead of request.form

Incorrect:

```python
request.method["name"]
```

Correct:

```python
request.form["name"]
```

`request.method` stores:

```
GET

POST
```

whereas `request.form` stores submitted form data.

---

## Missing name Attribute

Incorrect:

```html
<input type="text">
```

Correct:

```html
<input
    type="text"
    name="name"
>
```

Without a `name`, Flask cannot retrieve the field value.

---

## Forgetting to Import request

Incorrect:

```python
from flask import Flask
```

Correct:

```python
from flask import Flask, request
```

Otherwise:

```
NameError: name 'request' is not defined
```

---

# Best Practices

- Use GET for retrieving information.
- Use POST for sending user data.
- Always validate user input.
- Give every input field a meaningful `name`.
- Keep form processing logic simple and organized.
- Separate HTML templates from backend logic.

---

# Key Takeaways

- HTTP methods define how clients communicate with servers.
- GET retrieves data, while POST submits data.
- Flask uses GET by default.
- The `request` object provides access to incoming HTTP requests.
- `request.method` identifies the request type.
- `request.form` retrieves submitted form values.
- Every form input should have a `name` attribute.
- Forms are the foundation of interactive web applications such as login pages, registration systems, search forms, and contact pages.