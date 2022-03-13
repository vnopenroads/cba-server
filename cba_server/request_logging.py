import os
import json
import datetime
from os.path import join, abspath, dirname


def get_log_dir():
    return abspath(join(dirname(__file__), "..", "log"))


def get_request_dir():
    remote_dir = join(get_log_dir(), "flask_requests")
    if os.path.isdir(remote_dir):
        return remote_dir
    return None


def log_request(request):
    request_dir = get_request_dir()
    if request_dir is None:
        return None

    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
    filename = join(request_dir, f"run_sections_request_{timestamp}")
    with open(filename, "w") as f:
        f.write(json.dumps(request.json))
    return timestamp


def log_response(response, id):
    request_dir = get_request_dir()
    if request_dir is None:
        return None
    filename = join(request_dir, f"run_sections_response_{id}")
    with open(filename, "w") as f:
        f.write(json.dumps(response.json))
