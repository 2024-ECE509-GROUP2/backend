#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files (see told it would be useful later)
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# create a super user (as default) but no password
python manage.py createsuperuser --username admin --email admin@example.com --noinput