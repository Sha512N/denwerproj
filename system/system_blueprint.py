import flask
from flask import Blueprint
from flask import render_template
from flask import request
from sqlalchemy.orm import sessionmaker
import markdown
from sqlalchemy import or_

from db.mapper import ENGINE
from db.mapper import ArchType, ArchDescription
from system.forms import Search

md = markdown.Markdown(safe_mode='escape', extensions=['nl2br'])

system_blueprint = Blueprint('system', __name__)


@system_blueprint.route('/data/<short_link>')
def index(short_link: str):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    data = session.query(ArchType, ArchDescription).join(ArchDescription, ArchDescription.ARCH_ID == ArchType.ID) \
        .filter(ArchType.SHORT_LINK == short_link) \
        .with_entities(ArchDescription.TEXT, ArchType.NAME, ArchType.ID, ArchType.PARENT_ID).all()
    if len(data) == 0:
        flask.abort(404)

    children = session.query(ArchType) \
        .filter(ArchType.PARENT_ID == data[0].ID).with_entities(ArchType.SHORT_LINK, ArchType.NAME).all()
    parent = session.query(ArchType) \
        .filter(ArchType.ID == data[0].PARENT_ID).with_entities(ArchType.SHORT_LINK, ArchType.NAME).all()
    children_data = []
    for child in children:
        children_data.append({'link': child.SHORT_LINK, 'name': child.NAME})
    if len(parent) != 0:
        parent_data = {'link': parent[0].SHORT_LINK, 'name': parent[0].NAME}
    else:
        parent_data = None

    session.close()
    return render_template("page.html",
                           text=md.convert(data[0].TEXT),
                           name=data[0].NAME,
                           children=children_data, parent=parent_data)


@system_blueprint.route('/contextual_search', methods=['GET', 'POST'])
def search():

    form = Search()

    if request.method == "GET":
        return render_template("search.html", sicForm=form)

    Session = sessionmaker(bind=ENGINE)
    session = Session()
    keywords = [''.join(e for e in word if e.isalnum()) for word in form.word.data.lower().split(" ")]

    keywords_condition = or_(*[ArchDescription.TEXT.ilike('% {} %'.format(keyword)) for keyword in keywords],
                             *[ArchType.NAME.ilike('% {} %'.format(keyword)) for keyword in keywords],
                             *[ArchType.NAME.ilike('{} %'.format(keyword)) for keyword in keywords],
                             *[ArchType.NAME.ilike('% {}'.format(keyword)) for keyword in keywords],
                             *[ArchDescription.TEXT.ilike('{} %'.format(keyword)) for keyword in keywords],
                             *[ArchDescription.TEXT.ilike('{} %'.format(keyword)) for keyword in keywords])

    found = session.query(ArchType, ArchDescription) \
        .join(ArchDescription, ArchDescription.ARCH_ID == ArchType.ID) \
        .filter(keywords_condition).with_entities(ArchDescription.TEXT, ArchType.NAME, ArchType.SHORT_LINK).all()

    results = [{'name': found_element.NAME,
                "link": found_element.SHORT_LINK,
                "text": md.convert(found_element.TEXT[0:100] + "...")} for found_element in found]

    session.close()
    return render_template("search_result.html",
                           results=results)