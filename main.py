from flask import Flask, render_template

from db.mapper import POSTGRE_SQL
from db.mapper import ENGINE, ArchType, ArchDescription
from sqlalchemy.orm import sessionmaker


def create_app():
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = POSTGRE_SQL
    application.config['SECRET_KEY'] = 'secret-key-goes-here'
    from index.index_blueprint import index_blueprint
    application.register_blueprint(index_blueprint)
    from system.system_blueprint import system_blueprint
    application.register_blueprint(system_blueprint)

    @application.errorhandler(404)
    @application.errorhandler(500)
    def page_not_found(e):
        return render_template("404.html"), 404

    application.register_error_handler(404, page_not_found)
    application.register_error_handler(500, page_not_found)

    return application


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)
