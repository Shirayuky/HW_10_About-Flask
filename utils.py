# описаны функции по загрузке данных из JSON файла
from __future__ import annotations
import json
from typing import List


def load_json() -> List[dict]:
    """Загружает список со словарями"""
    path = 'candidates.json'

    with open(path, 'r', encoding='utf-8') as file:
        candidates = list(json.load(file))
        return candidates


def get_page_candidate(candidates: List[dict]) -> str:
    """Вывод 1-го кандидата по id"""
    result = '<pre>'

    for candidate in candidates:
        result += f"""
                {candidate['name']}\n
                {candidate['position']}\n
                {candidate['skills']}\n
            """
    result += '</pre>'
    return result


def get_all_candidates() -> List[dict]:
    """Включает загрузку джсон в лист"""
    return load_json()

def get_candidate_by_id(uid: int) -> dict | None:
    candidates = get_all_candidates()
    for candidate in candidates:
        if uid == candidate['id']:
            return candidate
    return None


def get_candidate_by_skills(skill: str) -> List[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill == candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

