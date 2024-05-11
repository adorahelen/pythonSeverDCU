from flask import render_template, redirect, url_for
from app import app  # Flask 애플리케이션 객체
from forms import RegistrationForm
from models import db, User

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))  # 회원가입 성공 시 로그인 페이지로 리다이렉트
    return render_template('register.html', title='Register', form=form)
