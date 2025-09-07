#!/bin/bash

# Create project root and subfolders
mkdir -p leadbot/services

# Create empty files
touch leadbot/app.py
touch leadbot/db.py
touch leadbot/services/openai_service.py
touch leadbot/services/crm_service.py
touch leadbot/services/notify_service.py
touch leadbot/models.sql
touch leadbot/requirements.txt
touch leadbot/Dockerfile
touch leadbot/.env.example

echo "✅ leadbot project structure created successfully!"
