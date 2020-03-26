"""
Live de Python #107 - Flask templates a vera - com StatusOK

Tutorial-Flask-templates-live-107

Homepage and documentation:
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

import os

from flask import Flask
from config import basedir


def create_app():
    app = Flask(__name__,
                template_folder=os.path.join(basedir, "src", "templates"),
                static_folder=os.path.join(basedir, "src", "static")
    )
    app.config['SECRET_KEY'] = 'testing'

    from app import routes

    routes.load(app)

    from app.filters import text_upper, text_truncate
    app.jinja_env.filters["text_truncate"] = text_truncate
    app.jinja_env.filters["text_upper"] = text_upper

    return app
