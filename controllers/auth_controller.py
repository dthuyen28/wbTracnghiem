from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if not email or not password:
            message = "Vui lòng nhập đầy đủ thông tin"
        else:
            message = "Đăng nhập thành công (demo)"

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
