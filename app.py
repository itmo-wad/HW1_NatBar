from flask import Flask, render_template, flash, request, redirect, url_for, session
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = b'lBb/=EKXg=1}Xz$nQb2Z_*e!O2>Xq%'

# Configure MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/wad"
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check username and password in MongoDB
        user = mongo.db.users.find_one({'username': username})

        if user:
            # Extract stored hash and salt from the user record
            stored_hash = user.get('hash', '')
            stored_salt = user.get('salt', '')

            # Check if the provided password matches the stored hash and salt
            if check_password_hash(stored_hash, stored_salt + password):
                # Authentication successful
                session['username'] = username
                return redirect(url_for('profile'))
            
    # Authentication failed, redirect back to login page
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    # Check if the user is authenticated
    if 'username' in session:
        return render_template('profile.html', username=session.get('username'))
    else:
        # Redirect to the login page if not authenticated
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    # Clear the session and redirect to the login page
    session.clear()
    return redirect(url_for('home'))
    
@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)