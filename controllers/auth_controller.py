from flask import Blueprint, render_template, request, redirect, url_for
from models.user_model import check_login

auth_bp = Blueprint(
    'auth',
    __name__,
    template_folder='../views'
)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = check_login(email, password)

        if user:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Sai email hoặc mật khẩu")

    return render_template('login.html')
