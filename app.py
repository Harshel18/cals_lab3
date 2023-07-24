from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database named users.db
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return f"<User {self.email}>"
    
with app.app_context():
    db.create_all()
    
def is_valid_password(password, confirm_password):
    if password != confirm_password:
        flash('Passwords do not match. Please try again.', 'error')
        return False
    elif len(password) < 8:
        flash('Password should be at least 8 characters long.', 'error')
        return False
    return True

def is_existing_user(email):
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        flash('Email already exists. Please try a different email.', 'error')
        return True
    return False

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            return redirect(url_for('secret_page'))
        else:
            flash('Invalid email or password. Please try again.', 'error')

    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if is_valid_password(password, confirm_password) and not is_existing_user(email):
            # Create a new user and add it to the database
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. You can now sign in.', 'success')
            return redirect(url_for('thank_you'))

    return render_template('signup.html')

@app.route('/secret', methods=['GET'])
def secret_page():
    return render_template('secretPage.html')

@app.route('/thankyou', methods=['GET'])
def thank_you():
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)
