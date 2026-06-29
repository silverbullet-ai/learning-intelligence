# Flask REST APIs & CRUD Operations

## Overview

REST APIs allow applications to communicate by exchanging data over HTTP. Unlike traditional Flask applications that return HTML pages, REST APIs primarily return JSON responses, making them suitable for web applications, mobile applications, desktop software, and microservices.

In this lesson, we build a simple Todo List REST API using Flask and implement all CRUD operations using HTTP methods.

---

## Topics Covered

- What is an API?
- REST APIs
- JSON
- Flask API Development
- HTTP Methods
- CRUD Operations
- GET Requests
- POST Requests
- PUT Requests
- DELETE Requests
- `jsonify()`
- `request.json`
- Variable Rules
- REST Client (VS Code)
- Postman
- API Testing
- REST Architecture

---

## What is an API?

API stands for **Application Programming Interface**.

It allows two different applications to communicate with each other.

Example:

```
Frontend
     │
     ▼
 REST API
     │
     ▼
Backend
```

Unlike traditional Flask applications that return HTML pages, APIs return structured data, usually in JSON format.

---

## Why Use APIs?

REST APIs allow communication between:

- Web Applications
- Mobile Applications
- Desktop Applications
- Microservices
- Machine Learning Models

Instead of:

```python
return render_template("index.html")
```

we return:

```python
return jsonify(data)
```

---

## What is JSON?

JSON (JavaScript Object Notation) is the most widely used format for exchanging data.

Example:

```json
{
    "id": 1,
    "name": "Laptop",
    "description": "Gaming Laptop"
}
```

JSON consists of key-value pairs and is lightweight, human-readable, and language-independent.

---

## Flask Modules

### requirements.txt

```Markdown
Flask
```

```python
from flask import Flask, jsonify, request
```

### Flask

Creates the Flask application.

### jsonify()

Converts Python objects into valid JSON responses.

### request

Reads incoming HTTP requests and JSON payloads.

---

## CRUD Operations

CRUD represents the four basic database operations.

| Operation | HTTP Method |
| --------- | ----------- |
| Create    | POST        |
| Read      | GET         |
| Update    | PUT         |
| Delete    | DELETE      |

---

## Sample Application Structure

```
Todo API

GET      /items
GET      /items/<id>

POST     /items

PUT      /items/<id>

DELETE   /items/<id>
```

---

## GET Request

Used to retrieve data.

### Get All Items

```python
GET /items
```

Returns every item.

### Get Single Item

```python
GET /items/<int:item_id>
```

Uses Flask Variable Rules.

---

## Using next()

```python
item = next(
    (
        item
        for item in items
        if item["id"] == item_id
    ),
    None
)
```

The `next()` function returns the first matching element from the generator expression.

If no match is found, it returns `None`.

---

## POST Request

Creates a new resource.

Example:

```json
{
    "name":"Laptop",
    "description":"Gaming Laptop"
}
```

The request body is accessed using:

```python
request.json
```

---

## request.json

Reads JSON data sent by the client.

Example:

```python
request.json["name"]
```

or

```python
request.json.get("name")
```

---

## PUT Request

Updates an existing resource.

```python
PUT /items/1
```

Generally uses:

```python
request.json.get()
```

to safely retrieve updated values.

---

## DELETE Request

Deletes a resource.

Example:

```python
DELETE /items/1
```

The lecture removes an item using list comprehension.

---

## jsonify()

Instead of:

```python
return items
```

use:

```python
return jsonify(items)
```

This converts Python objects into proper JSON responses.

---

## Testing APIs

### Browser

Supports only:

- GET

### REST Client (VS Code)

Supports:

- GET
- POST
- PUT
- DELETE

using `.http` files.

### Postman

Professional API testing tool used for:

- API Testing
- Authentication
- Collections
- Environment Variables
- Documentation

---

## REST Client Example

```http
GET http://127.0.0.1:5000/items
```

Each request can be separated using:

```http
###
```

---

## REST Architecture

```
Client
   │
   ▼
HTTP Request
   │
   ▼
Flask Route
   │
   ▼
Business Logic
   │
   ▼
JSON Response
   │
   ▼
Client
```

---

## Browser vs Postman

| Feature | Browser | Postman |
| ------- | ------- | ------- |
| GET     | ✅      | ✅      |
| POST    | ❌      | ✅      |
| PUT     | ❌      | ✅      |
| DELETE  | ❌      | ✅      |

---

## Common Errors

### Missing JSON Body

```python
if not request.json
```

### Missing Required Field

```python
"name" not in request.json
```

### Forgetting jsonify()

Returning raw Python objects instead of JSON.

---

## One-Line Summary

REST APIs allow applications to exchange data using HTTP methods, with Flask providing a simple way to build CRUD APIs that communicate through JSON.