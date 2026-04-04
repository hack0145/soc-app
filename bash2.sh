#!/bin/bash

# # Path to your server logs
# LOG_FILE="app.log"

# Slack Webhook URL
WEBHOOK_URL="url"


# Message to send
MESSAGE="Hello, Slack! This is a message from my Bash script."

# Send the message using curl
curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$MESSAGE\"}" $WEBHOOK_URL
