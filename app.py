from flask import Flask, render_template, request
import random

app = Flask(__name__)

questions = [

{"q":"Who is the last Prophet in Islam?",
"options":["Prophet Musa","Prophet Isa","Prophet Muhammad","Prophet Ibrahim"],
"answer":"Prophet Muhammad"},

{"q":"What is the holy book of Islam?",
"options":["Bible","Torah","Quran","Vedas"],
"answer":"Quran"},

{"q":"How many pillars of Islam are there?",
"options":["3","4","5","6"],
"answer":"5"},

{"q":"Where was Prophet Muhammad born?",
"options":["Madinah","Makkah","Taif","Jerusalem"],
"answer":"Makkah"},

{"q":"How many daily prayers are obligatory?",
"options":["3","4","5","6"],
"answer":"5"},

{"q":"Which angel revealed the Quran?",
"options":["Jibreel","Mikaeel","Israfeel","Azrael"],
"answer":"Jibreel"},

{"q":"What is the fasting month called?",
"options":["Ramadan","Shaban","Muharram","Rajab"],
"answer":"Ramadan"},

{"q":"What is the direction Muslims pray toward?",
"options":["Jerusalem","Kaaba","Madinah","Mount Sinai"],
"answer":"Kaaba"},

{"q":"Which city is called the City of the Prophet?",
"options":["Makkah","Madinah","Taif","Cairo"],
"answer":"Madinah"},

{"q":"What is Zakat?",
"options":["Prayer","Charity","Fasting","Pilgrimage"],
"answer":"Charity"}
]

questions = questions * 3   # 30 questions


@app.route("/")
def quiz():

    random.shuffle(questions)

    return render_template(
        "quiz.html",
        questions=questions
    )


@app.route("/result", methods=["POST"])
def result():

    score = 0

    for i,q in enumerate(questions):

        user = request.form.get(f"q{i}")

        if user == q["answer"]:
            score += 1

    total = len(questions)
    percent = int((score/total)*100)


        # Greeting message logic
    if percent >= 80:
        message = "MashaAllah! Excellent knowledge of Islam 🌙"
    elif percent >= 50:
        message = "Good effort! Keep learning and improving 📖"
    else:
        message = "Don't worry! Keep studying Islam and try again 🤲"

    return render_template(
        "result.html",
        score=score,
        total=total,
        percent=percent,
        message=message
    )