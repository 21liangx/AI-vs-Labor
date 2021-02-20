from flask import Flask, render_template, request, Response
import calculation
import json
from wtforms import TextField, Form
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)

class SearchForm(Form):
    job = TextField('JOB', id='job_autocomplete')

jobs = calculation.get_jobs()

@app.route('/_autocomplete', methods=['GET', 'POST'])
def autocomplete():
    print(jobs)
    return Response(json.dumps(jobs), mimetype='application/json')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)

class Job(Resource):
    def get(self):
        return Response(json.dumps(jobs), mimetype='application/json')

api.add_resource(Job, '/names')

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/reqest", methods=['GET', 'POST'])
def req():
    form = SearchForm(request.form)
    return render_template("req.html", form=form)

@app.route("/report", methods=["GET","POST"])
def report():
    if request.method == "GET":
        return "<h2 style='text-align: center;color: red;'>Please submit the form instead.</h2>"
    else:
        name = request.form.get("name")
        gender = request.form.get("gender")
        race = request.form.get("race")
        occupation = str(request.form["job"])
        age = int(request.form.get("age"))
        if calculation.check_job(occupation)==False:
            text = "Your job is not found. Please try again."
            form = SearchForm(request.form)
            return render_template("req.html",text=text, form=form)
        pGender = calculation.get_gender(gender)
        pComputerisation = calculation.get_computerisation(occupation)
        pAge = calculation.get_age(age)
        pRace = calculation.get_race(race)
        pFinal = calculation.main(gender, age, race, occupation)
        return render_template("report.html", name=name,pGender=pGender,pRace=pRace,pComputerisation=pComputerisation,pFinal=pFinal,pAge=pAge)
        #https://halfbothalfbrain.netlify.app/
        #return "<h2>Report: {} {} {} {} {}!<h2>".format(name, gender, race, age, occupation)
