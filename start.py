from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.php')

@app.route('/login')
def login():
    return render_template('login.php')

@app.route('/register')
def register():
    return render_template('register.php')

if __name__ == '__main__':
    app.run(debug=True)
