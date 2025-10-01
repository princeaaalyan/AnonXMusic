#!/bin/bash
# Render startup script for AnonXMusic Bot

echo "Starting AnonXMusic Bot on Render..."

# Set working directory
cd /opt/render/project/src

# Install dependencies if needed
pip install -r requirements.txt

# Start the bot
echo "Launching AnonXMusic Bot..."
python3 -m AnonXMusic
