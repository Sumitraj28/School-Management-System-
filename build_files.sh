#!/bin/bash

set -e  # Exit on any error

echo "==> Installing Python dependencies..."
python3.9 -m pip install -r requirements.txt

echo "==> Collecting static files..."
python3.9 manage.py collectstatic --noinput

echo "==> Running database migrations..."
python3.9 manage.py migrate

echo "==> Build complete!"
