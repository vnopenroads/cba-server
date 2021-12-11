from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for,
    jsonify,
)
from werkzeug.exceptions import abort
import pandas as pd
import json
import sys
import math

from cba_server.db import get_db
from cba_server.request_logging import log_request, log_response
from roads_cba_py.section import Section, InvalidSection, parse_section
from roads_cba_py.cba import CostBenefitAnalysisModel
from roads_cba_py.utils import flatten, split_on_condition
from roads_cba_py.config import Config


bp = Blueprint("api", __name__)


@bp.route("/run_sections", methods=["POST"])
def run_sections():
    request_id = log_request(request)
    config = Config.parse_obj(request.json["config"])
    assets = request.json["assets"]
    valid_sections, invalid_sections, stats = split_assets_by_validity(assets)

    cba = CostBenefitAnalysisModel(config)
    results = [cba.compute_cba_for_section(s) for s in valid_sections]
    results = sorted(results, key=lambda x: (x.work_year, -x.npv_cost))

    problems = flatten([s.invalid_reason() for s in invalid_sections])
    invalid_reasons = pd.DataFrame(data=problems, columns=["reason"])
    invalid_reasons = invalid_reasons["reason"].value_counts().to_dict()

    response = jsonify(
        {
            "stats": stats,
            "invalids": invalid_reasons,
            "data": [s.dict() for s in results],
        }
    )
    log_response(response, request_id)

    return response


@bp.route("/evaluate_assets", methods=["POST"])
def evaluate_assets():
    _valid_sections, invalid_sections, stats = split_assets_by_validity(request.json)

    problems = flatten([s.invalid_reason() for s in invalid_sections])
    invalid_reasons = pd.DataFrame(data=problems, columns=["reason"])
    invalid_reasons = invalid_reasons["reason"].value_counts().to_dict()
    return jsonify({"stats": stats, "invalids": invalid_reasons})


def split_assets_by_validity(data):
    sections = [parse_section(s) for s in data]
    valid_sections, invalid_sections = split_on_condition(sections, lambda s: s.invalid_reason() is None)

    stats = {"valid": len(valid_sections), "invalid": len(invalid_sections)}
    return (valid_sections, invalid_sections, stats)
