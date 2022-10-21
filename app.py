# приложение и все роуты
from flask import Flask
import utils
from typing import List


app = Flask(__name__)

@app.route("/")
def page_header():
    """Главная страница"""
    candidates: List[dict] = utils.get_all_candidates()
    result: str = utils.get_page_candidate(candidates)
    return result


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    """Поиск кандидата по id"""
    candidate: dict = utils.get_candidate_by_id(uid)
    result: str = f'<img src="{candidate["picture"]}">'
    result += utils.get_page_candidate([candidate])
    return result


@app.route("/skills/<skill>")
def page_skills(skill):
    """Поиск кандидата по навыку"""
    skill_lower = skill.lower()
    candidate: List[dict] = utils.get_candidate_by_skills(skill_lower)
    result = utils.get_page_candidate(candidate)
    return result


app.run()