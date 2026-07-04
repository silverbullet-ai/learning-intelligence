# Flask Dynamic Routing & Jinja2

## Overview

Modern web applications rarely display the same content to every user. Instead, they generate dynamic pages based on user input, URL parameters, and backend data.

Flask provides several features that make this possible:

- Form Action Attribute
- Dynamic URLs
- Variable Rules
- URL Parameters
- `redirect()`
- `url_for()`
- Jinja2 Template Engine
- Passing Data from Flask to HTML
- Jinja2 Expressions
- Jinja2 Control Statements

Together, these features allow Flask applications to create personalized and interactive web experiences.

---

# Form Action Attribute

Previously, forms were written as:

```html
<form method="POST">
```

In this case, the form submits to the current URL.

Example:

```
Current URL

↓

/form

↓

POST

↓

/form
```

---

## Using the action Attribute

Instead of submitting to the same page, a form can send data to another route.

Example:

```html
<form action="/submit" method="POST">
```

Now the request flow becomes:

```
User Fills Form

↓

Submit

↓

POST /submit

↓

Flask Route

↓

Response
```

This is useful when:

- One route displays the form
- Another route processes the submitted data

---

## Example

HTML

```html
<form action="/submit" method="POST">

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

Flask

```python
@app.route("/submit", methods=["GET", "POST"])
def submit():

    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}"
```

---

# Dynamic URLs

Most websites do not have fixed URLs.

Instead of:

```
/student1

/student2

/student3
```

we prefer:

```
/student/<id>
```

Flask supports this using **Variable Rules**.

---

# Variable Rules

Variable Rules allow parts of a URL to become dynamic.

Example:

```python
@app.route("/success/<score>")
def success(score):

    return f"Marks = {score}"
```

Visiting:

```
http://127.0.0.1:5000/success/55
```

produces:

```
Marks = 55
```

---

## How It Works

URL:

```
/success/55
```

Flask automatically extracts:

```
score = "55"
```

and passes it as a parameter to the function.

---

# Default Data Type

Without specifying a converter:

```python
@app.route("/success/<score>")
```

everything is treated as a string.

These URLs all work:

```
/success/55

/success/Aahish

/success/python
```

because:

```
score → str
```

---

# Type Converters

Flask allows URL parameters to be restricted to specific data types.

Example:

```python
@app.route("/success/<int:score>")
```

Now only integers are accepted.

Valid:

```
/success/55
```

Invalid:

```
/success/python
```

Result:

```
404 Not Found
```

because the converter expects an integer.

---

# Available Converters

| Converter | Description |
|-----------|-------------|
| string | Default string type |
| int | Integer values |
| float | Floating-point values |
| path | File paths |
| uuid | UUID values |

Examples:

```python
@app.route("/user/<int:id>")
```

```python
@app.route("/price/<float:value>")
```

---

# String Concatenation Problem

Suppose:

```python
@app.route("/success/<int:score>")
```

This means:

```
score → int
```

Incorrect:

```python
return "Marks = " + score
```

Error:

```
TypeError

can only concatenate str (not "int") to str
```

Correct:

```python
return "Marks = " + str(score)
```

or

```python
return f"Marks = {score}"
```

Using f-strings is the preferred approach.

---

# Jinja2 Template Engine

Flask uses **Jinja2** to generate dynamic HTML pages.

Instead of:

```python
return f"Hello {name}"
```

we can send data to an HTML template.

Python:

```python
return render_template(
    "result.html",
    name=name
)
```

HTML:

```html
<h1>Hello {{ name }}</h1>
```

Output:

```
Hello Aahish
```

---

# Passing Data to Templates

Python:

```python
result = "Pass"

return render_template(
    "result.html",
    results=result
)
```

HTML:

```html
<h1>{{ results }}</h1>
```

Output:

```
Pass
```

---

# Jinja2 Expressions

Expressions display values inside HTML.

Syntax:

```jinja2
{{ variable }}
```

Example:

```html
<h2>{{ username }}</h2>
```

Output:

```
Aahish
```

---

# Jinja2 Control Statements

Control statements allow conditional logic and loops inside templates.

Syntax:

```jinja2
{% ... %}
```

Examples include:

- if
- else
- for

---

# If Statement

Python:

```python
return render_template(
    "result.html",
    score=55
)
```

HTML:

```jinja2
{% if score >= 50 %}

<h2>Pass</h2>

{% else %}

<h2>Fail</h2>

{% endif %}
```

Output:

```
Pass
```

---

# For Loop

Python:

```python
student = {
    "score": 88,
    "result": "Pass"
}

return render_template(
    "result.html",
    results=student
)
```

HTML:

```jinja2
{% for key, value in results.items() %}

<h3>{{ key }}</h3>
<p>{{ value }}</p>

{% endfor %}
```

Output:

```
score

88

result

Pass
```

This is useful when displaying dictionaries, reports, API responses, or dashboards.

---

# Jinja2 Comments

Comments inside templates are written as:

```jinja2
{# This comment will not appear in the browser #}
```

Unlike HTML comments, Jinja2 comments are completely removed during rendering.

---

# Dynamic URL Generation

Hardcoding URLs is not recommended.

Instead of:

```python
redirect("/success/55")
```

Flask provides `url_for()`.

---

# url_for()

Purpose:

Generate URLs using route function names instead of hardcoded paths.

Example:

```python
url_for(
    "success",
    score=55
)
```

Generated URL:

```
/success/55
```

Benefits:

- No hardcoded URLs
- Easier maintenance
- Safer refactoring
- Automatic URL generation

---

# redirect()

The `redirect()` function sends the user to another route.

Example:

```python
return redirect(
    url_for(
        "success",
        score=55
    )
)
```

Workflow:

```
Current Route

↓

redirect()

↓

url_for()

↓

Generated URL

↓

Browser Redirect

↓

New Route
```

---

# Student Result Application

Example workflow:

```
Student Enters Marks

↓

POST Request

↓

Calculate Average

↓

Determine Result

↓

redirect()

↓

success()

↓

render_template()

↓

Display Result
```

Average calculation:

```python
average = (
    science +
    maths +
    c +
    data_science
) / 4
```

Then:

```python
return redirect(
    url_for(
        "success",
        score=average
    )
)
```

---

# Complete Flow

```
HTML Form

↓

POST Request

↓

request.form

↓

Calculate Result

↓

redirect()

↓

url_for()

↓

Dynamic Route

↓

render_template()

↓

Jinja2

↓

Browser
```

---

# Common Beginner Mistakes

## Hardcoding URLs

Incorrect:

```python
redirect("/success/80")
```

Preferred:

```python
redirect(
    url_for(
        "success",
        score=80
    )
)
```

---

## Forgetting Type Conversion

Incorrect:

```python
return "Marks = " + score
```

Correct:

```python
return f"Marks = {score}"
```

---

## Incorrect Variable Name

Python:

```python
return render_template(
    "index.html",
    name="Aahish"
)
```

HTML:

```html
{{ username }}
```

Nothing will be displayed because the variable names do not match.

---

## Forgetting Control Statement Terminators

Always close blocks:

```jinja2
{% endif %}
```

```jinja2
{% endfor %}
```

---

# Best Practices

- Use `url_for()` instead of hardcoded URLs.
- Use f-strings when displaying variables.
- Pass data through `render_template()`.
- Keep business logic inside Python, not HTML.
- Use Jinja2 only for presentation logic.
- Keep templates clean and readable.

---

# Key Takeaways

- Forms can submit data to different routes using the `action` attribute.
- Variable Rules allow URLs to accept dynamic parameters.
- Flask supports type converters such as `int`, `float`, and `string`.
- Jinja2 is Flask's default template engine.
- `{{ }}` displays variables inside HTML.
- `{% %}` is used for control statements such as `if` and `for`.
- `{# #}` creates Jinja2 comments.
- `url_for()` dynamically generates URLs.
- `redirect()` sends users to another route.
- Jinja2 bridges Flask backend data with HTML templates, making web pages dynamic and interactive.