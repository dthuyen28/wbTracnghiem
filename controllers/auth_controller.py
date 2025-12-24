from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user_model import check_login, is_email_exists, add_user

auth_bp = Blueprint("auth", __name__, template_folder='../')

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = check_login(email, password)
        if user:
            session["user"] = user
            return redirect("/dashboard")
        else:
            message = "Sai email hoặc mật khẩu"
    return render_template("login.html", message=message)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        if not fullname or not email or not password:
            message = "Vui lòng nhập đầy đủ thông tin"
        else:
            message = "Đăng ký thành công (demo)"

    return render_template("register.html", message=message)
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))