import os
import json
import datetime
from pathlib import Path


def get_request_dir():
    remote_dir = "/home/ubuntu/log/flask_requests"
    if os.path.isdir(remote_dir):
        return remote_dir
    return str(Path.home())


def log_request(request):
    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
    filename = os.path.join(get_request_dir(), f"run_sections_{timestamp}")
    with open(filename, "w") as f:
        f.write(json.dumps(request.json))
