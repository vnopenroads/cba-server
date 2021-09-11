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
import math

from cba_server.db import get_db
from roads_cba_py.section import Section, InvalidSection, parse_section
from roads_cba_py.cba import CostBenefitAnalysisModel
from roads_cba_py.utils import flatten, split_on_condition


bp = Blueprint("api", __name__)


@bp.route("/run_sections", methods=["POST"])
def run_sections():
    valid_sections, invalid_sections, stats = split_assets_by_validity(request.json)

    cba = CostBenefitAnalysisModel()
    results = [cba.compute_cba_for_section(s) for s in valid_sections]

    valid_results, invalid_results = split_on_condition(results, lambda r: not math.isnan(r.eirr))

    problems = flatten([s.invalid_reason() for s in invalid_sections]) + ["eirr is NaN"] * len(invalid_results)
    invalid_reasons = pd.DataFrame(data=problems, columns=["reason"])
    invalid_reasons = invalid_reasons["reason"].value_counts().to_dict()

    return jsonify(
        {
            "stats": stats,
            "invalids": invalid_reasons,
            "data": [s.to_primitive() for s in valid_results],
        }
    )


@bp.route("/evaluate_assets", methods=["POST"])
def evaluate_assets():
    _valid_sections, invalid_sections, stats = split_assets_by_validity(request.json)
    return jsonify({"stats": stats, "invalids": invalid_sections})


def split_assets_by_validity(data):
    sections = [parse_section(s) for s in data]
    valid_sections, invalid_sections = split_on_condition(sections, lambda s: s.invalid_reason() is None)

    stats = {"valid": len(valid_sections), "invalid": len(invalid_sections)}
    return (valid_sections, invalid_sections, stats)
