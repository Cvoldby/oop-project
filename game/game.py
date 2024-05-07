from flask import (
    redirect, render_template, Blueprint, flash, g, redirect, render_template, request, url_for
)

from game.auth import login_required
from game.db import get_db

from game.game_classes import *

bp = Blueprint('race', __name__, url_prefix='/race')

