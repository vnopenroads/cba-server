#!/usr/bin/env bash

set -eu

main() {
  source venv/bin/activate
  FLASK_APP=cba_server FLASK_ENV=development flask run
}

main "$@"
