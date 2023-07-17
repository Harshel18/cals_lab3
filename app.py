from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    username = request.form.get('username')
    password = request.form.get('password')

    password_requirements = {
        'Lowercase': check_lowercase(password),
        'Uppercase': check_uppercase(password),
        'Ends with Digit': check_ends_with_digit(password),
        'Length >= 8': check_length(password)
    }

    password_passed = all(password_requirements.values())
    missing_requirements = get_missing_requirements(password_requirements)

    return render_template('report.html', username=username, password_passed=password_passed, missing_requirements=missing_requirements)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_ends_with_digit(password):
    return password[-1].isdigit()

def check_length(password):
    return len(password) >= 8


def get_missing_requirements(password_requirements):
    return [requirement for requirement, passed in password_requirements.items() if not passed]



if __name__ == '__main__':
    app.run(debug=True)
