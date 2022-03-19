from flask import Flask

import utils

app = Flask(__name__)

candidates = utils.load_candidates()


@app.route("/")
def main_page():
    tag = "<pre>"
    for candidate in candidates.values():
        tag += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n \n"
    tag += "</pre>"
    return tag


@app.route("/candidates/<int:id>")
def profile(id):
    candidate = candidates[id]
    tag = f"<img src={candidate['picture']}></img <br><br>{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']}<br><br>"

    return tag


@app.route("/skills/<skill>")
def skill_profile(skill):
    tag = '<pre>'
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill in candidate_skills:
            tag += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n \n"

    tag += "</pre>"
    return tag


app.run()
