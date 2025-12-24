from flask import Blueprint, render_template, request, redirect, url_for
import json
import os

question_bp = Blueprint(
    'question',
    __name__,
    url_prefix='/question'
)

DATA_FILE = 'data/questions.json'


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"questions": []}
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


@question_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        question = request.form.get('question')
        a = request.form.get('a')
        b = request.form.get('b')
        c = request.form.get('c')
        d = request.form.get('d')
        correct = request.form.get('correct')

        if not all([question, a, b, c, d, correct]):
            return "Vui lòng nhập đầy đủ dữ liệu"

        data = load_data()

        new_question = {
            "id": len(data["questions"]) + 1,
            "content": question,
            "answers": {
                "A": a,
                "B": b,
                "C": c,
                "D": d
            },
            "correct": correct
        }

        save_data(data)

        return redirect(url_for('question.add'))

    return render_template('question.html')

@question_bp.route("/edit", methods=["GET", "POST"])
def edit_question( ):
    if request.method == "POST":
        return redirect("/dashboard")
   
    return render_template("edit_question.html")