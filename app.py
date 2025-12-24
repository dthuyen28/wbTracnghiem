from flask import Flask, redirect, url_for,render_template,session
from controllers.auth_controller import auth_bp
from controllers.question_controller import question_bp


app = Flask(__name__, template_folder='views')
app.secret_key = 'secret_key'

app.register_blueprint(auth_bp)
app.register_blueprint(question_bp) 

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

@app.route('/dashboard')
def dashboard():
        if 'user' not in session:
             return redirect(url_for('auth.login'))
        return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
