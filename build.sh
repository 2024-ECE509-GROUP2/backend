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
python manage.py createsuperuser --username admin1 --email admin1@example.com --noinput
if [ $? -ne 0 ]; then
  echo "Failed to Create SuperUser, Might Already Have Been Created continuing anyway..."
fi