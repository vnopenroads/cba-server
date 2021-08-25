from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
import pandas as pd

from cba_server.db import get_db
from roads_cba_py.section import Section, InvalidSection
from roads_cba_py.cba import CostBenefitAnalysisModel

bp = Blueprint('api', __name__)

@bp.route('/run_sections', methods=['POST'])
def run_sections():
    valid_sections, invalid_sections,stats = split_assets_by_validity(request.json)
    cba = CostBenefitAnalysisModel()
    results = [cba.compute_cba_for_section(s) for s in valid_sections]

    return jsonify({ "stats": stats, "invalids": invalid_sections, "data": [s.to_primitive() for s in results] })

@bp.route('/evaluate_assets', methods=['POST'])
def evaluate_assets():
    valid_sections, invalid_sections,stats = split_assets_by_validity(request.json)
    return jsonify({ "stats": stats, "invalids": invalid_sections })

@bp.route('/jamie', methods=['GET'])
def jamie():
    return jsonify({"answer": 42})

def parse_section(json):
    try:
        return Section(json)
    except Exception as err:
        return InvalidSection([str(err)], json)

def split_assets_by_validity(data): 
    sections = [parse_section(s) for s in data]
    sections = [(s,s.invalid_reason()) for s in sections]

    valid_sections = [s for (s,r) in sections if r is None]
    invalid_sections = [(s,r) for (s,r) in sections if r is not None]

    stats = {"valid": len(valid_sections), "invalid": len(invalid_sections) }
    invalids = pd.DataFrame(data=flatten([r for (s,r) in invalid_sections]), columns=['reason'])
    invalids = invalids['reason'].value_counts().to_dict()
    return (valid_sections, invalids, stats)
 
def flatten(a_of_a):
    return [x for y in a_of_a for x in y]