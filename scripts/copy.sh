#!/bin/bash

NEW_PROJECT="django-project-${$1}"

cp -r django-project "${NEW_PROJECT}"

rm -rf "${NEW_PROJECT}/.idea" "${NEW_PROJECT}/.pytest_cache" "${NEW_PROJECT}/.git" "${NEW_PROJECT}/.venv" "${NEW_PROJECT}/.db.sqlite3"

find "${NEW_PROJECT}" -type d -name __pycache__ -prune -exec rm -rf {} +