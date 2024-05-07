from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from game.auth import login_required
from game.db import get_db

bp = Blueprint('bet', __name__)

