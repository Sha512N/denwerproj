import flask
from flask import Blueprint
from flask import render_template
from sqlalchemy.orm import sessionmaker
import markdown

from db.mapper import ENGINE
from db.mapper import ArchType, ArchDescription
md = markdown.Markdown(safe_mode='escape',extensions=['nl2br'])

system_blueprint = Blueprint('system', __name__)


@system_blueprint.route('/<short_link>')
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
