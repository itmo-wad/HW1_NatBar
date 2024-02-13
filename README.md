## Frontend: creation of a static profile page about myself (HTML + CSS)
### 1. Creation of HTML-file.
Such tegs as `<html>, <head>, <body>, <h1>, <h2>, <div>, <blockquote>, <p>, <ul>, <li>` were used. I have written some info about my skills, experience and eduacation.
### 2. The design of my profile page choice.
Some style was applied. I have changed color, size, weight of the font, used GIF as background image and so on.
### 3. Aplication of the stylesheet.
Using the teg `<link>`: `<link rel="stylesheet" href="../static/css/styles.css">`.

## Backend: using Python Flask to serve the frontend (profile page)
### 4. Installing a micro web framework Flask.
The easiest thing ever - installing via `pip`.
### 5. Serving static profile page.
I have used `render_template` to serve my profile page at default (`/`) route.
### 6. Serving images, CSS files as static resources.
And this is the tree of the directories and files that I have got:
.
├───static
│   ├───css
│   │   └───styles.css
│   └───images
│       └───space.gif
├───templates
│   └───index.html
├───app.py
└───README.md
### 7. Serving profile page at '/profile' and redirect default route to it.
I have used such functions as `redirect` and `url_for` to redirect default route to page '/profile'. This is how I have made it:
```
@app.route('/profile')
def index():
    return render_template("index.html")

@app.route('/')
def redirect_to_profile():
    return redirect(url_for('index'))
```




