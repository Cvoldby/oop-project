import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "game.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exits when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # a simple home page
    @app.route("/")
    def home():
        #html = open("templates/home.html", "r").read()
        return render_template('home.html')
    
    # database stuff
    from . import db
    db.init_app(app)


    # authentication stuff
    from . import auth
    app.register_blueprint(auth.bp)


    return app    