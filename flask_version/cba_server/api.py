from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from cba_server.db import get_db
from roads_cba_py.cba import test_api

bp = Blueprint('api', __name__)

@bp.route('/test_api', methods=['POST'])
def hello():
    data = request.json
    input = data['key']
    output = test_api(input)

    return f"You provided {input} which I processed into {output}"
