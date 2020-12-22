from flask import render_template, request
from application import app
from application.model.entity.disciplina import Disciplina
from application.model.dao.disciplina_dao import DisciplinaDAO
from application import listaDisciplinas


@app.route('/')
def home():
    disciplina_dao = DisciplinaDAO()
    for disciplina in listaDisciplinas:
        disciplina_id = disciplina.get_id()
    disciplina = disciplina_dao.buscar_por_id(disciplina_id)