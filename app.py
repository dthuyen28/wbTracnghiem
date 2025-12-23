from flask import Flask, redirect, url_for
from controllers.auth_controller import auth_bp


app = Flask(__name__, template_folder="views")
app.secret_key = "secret_key"

app.register_blueprint(auth_bp)


@app.route("/")
def index():
    return redirect(url_for("auth.register"))

if __name__ == "__main__":
    app.run(debug=True)
