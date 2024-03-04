from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secret key for session security

# Dummy user data (Replace this with a proper user authentication mechanism)
users = {
    'admin': 'admin123'
}

# Store questions and answers
questions = []
answers = []

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', questions=questions)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Add_question and create_exam routes remain the same...

if __name__ == '__main__':
    app.run(debug=True)
