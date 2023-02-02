from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def root():
    """ Render the home page to start survey """
    
    return render_template("home.html", survey = survey )


@app.route("/start_survey")
def start():
    """Started survey and showed first question"""
    
    return redirect('/questions/0') 

@app.route("/questions/<int:id>")
def handle_q(id):
    print("id is" ,id)
    if id == len(responses):
        return render_template('questions.html', survey = survey , id=id )
    elif len(responses) == len(survey.questions):
        flash("You have already completed the Survey!")
        return redirect('/thanks')
    else: 
        flash("Not available, Please continue here.")
        return redirect(f"/questions/{len(responses)}")
    
    
@app.route("/answer", methods=["post"])
def handle_answer():
    
    res = request.form["answer"]
    responses.append(res)
    
    if len(responses) == len(survey.questions):
        return redirect('/thanks')
    else:
        return redirect(f"/questions/{len(responses)}")
    
@app.route('/thanks')
def say_thanks():
    
    # responses = []
    return render_template('thanks.html', survey=survey)
