from flask import (
    Flask, redirect, render_template, Blueprint, flash, g, redirect, render_template, request, url_for
)

from game.auth import login_required
from game.db import get_db

from game.game_classes import *

bp = Blueprint('race', __name__, url_prefix='/race')

app = Flask.app(__name__)

@app.route('/game')
def game():
    return render_template('game_page/main_game.html')


@app.route('/update_position')
def method_name():
    
    return render_template('game_page/main_game.html')