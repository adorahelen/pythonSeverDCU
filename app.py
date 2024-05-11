from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/')
def home():
    # render_template 함수를 사용하여 base.html을 렌더링하고 클라이언트에게 반환
    return render_template('base.html')

@app.route('/register')
def register():
    # render_template 함수를 사용하여 register.html을 렌더링하고 클라이언트에게 반환
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
