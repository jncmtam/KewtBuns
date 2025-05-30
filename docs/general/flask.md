In Flask, the term “methods” usually refers to two things:

### 1. **HTTP Methods**

When defining routes, Flask lets you specify which HTTP methods (like `GET`, `POST`, etc.) are allowed. These are the most commonly used:

* **GET**: Retrieve data (default method).
* **POST**: Submit data to be processed (e.g., from a form).
* **PUT**: Update an existing resource.
* **DELETE**: Delete a resource.
* **PATCH**: Partially update a resource.
* **OPTIONS**: Check what methods are supported.

Example:

```python
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return 'Data submitted!'
    return 'Submit Form'
```

---

### 2. **Common Flask Functions/Methods**

Here are some usual methods or utilities used in Flask apps:

#### a. **Routing and View Functions**

* `@app.route()` – Define a route.
* `url_for()` – Get a URL from a function name.
* `redirect()` – Redirect to another route.
* `render_template()` – Render an HTML template.

#### b. **Request and Response**

* `request.method` – Check if it’s GET or POST.
* `request.form` – Access form data.
* `request.args` – Access query string.
* `request.json` – Access JSON data.
* `make_response()` – Customize HTTP response.

#### c. **Session and Cookies**

* `session` – Store user-specific data (needs a secret key).
* `request.cookies` and `make_response().set_cookie()` – Cookie handling.

#### d. **Error Handling**

* `abort()` – Raise HTTP error like 404.
* `@app.errorhandler()` – Custom error pages.

#### e. **Blueprints** – Modularizing your app.

* `Blueprint()` – Organize your app into components.

---

If you're doing something specific like auth, file uploads, or APIs, Flask has typical patterns for those too. Let me know if you want examples in those areas!
