import os
import json
import datetime
from pathlib import Path


def get_request_dir():
    remote_dir = "/home/ubuntu/log/flask_requests"
    if os.path.isdir(remote_dir):
        return remote_dir

    return os.path.dirname(os.path.realpath(__file__))


def log_request(request):
    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
    filename = os.path.join(get_request_dir(), f"run_sections_request_{timestamp}")
    print(filename)
    with open(filename, "w") as f:
        f.write(json.dumps(request.json))
    return timestamp


def log_response(response, id):
    filename = os.path.join(get_request_dir(), f"run_sections_response_{id}")
    with open(filename, "w") as f:
        f.write(json.dumps(response.json))
