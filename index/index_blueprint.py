from flask import Blueprint
from flask import render_template
from sqlalchemy.orm import sessionmaker

from db.mapper import ENGINE
from db.mapper import ArchType

index_blueprint = Blueprint('index', __name__)


def find_children(element: ArchType, session):
    data = session.query(ArchType).filter(ArchType.PARENT_ID == element.ID).all()
    if len(data) == 0:
        return {}
    tree_data = {}
    for tree_element in data:
        tree_data[tree_element.SHORT_LINK] = {"name": tree_element.NAME, "children": find_children(tree_element, session)}
    return tree_data


def append_childred(element: ArchType, session, tree_data: dict):
    data = session.query(ArchType).filter(ArchType.PARENT_ID == element.ID).all()
    if len(data) == 0:
        return
    for tree_element in data:
        tree_data['nodes'].append({"link": tree_element.SHORT_LINK, "name": tree_element.NAME})
        tree_data['nodes'].append({"indent": True})
        append_childred(tree_element, session, tree_data)
        tree_data['nodes'].append({"outdent": True})
    return


@index_blueprint.route('/')
def index():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    data = session.query(ArchType).filter(ArchType.PARENT_ID == None).all()
    tree_data = {"nodes": []}
    for tree_element in data:
        tree_data['nodes'].append({"link": tree_element.SHORT_LINK, "name": tree_element.NAME})
        tree_data['nodes'].append({"indent": True})
        append_childred(tree_element, session, tree_data)
        tree_data['nodes'].append({"outdent": True})
    session.close()
    return render_template("index.html", tree_data=tree_data)
