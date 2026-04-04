#!/bin/bash

# Set the log file location
LOG_FILE="app.log"

# Set the Slack webhook URL (replace with your actual webhook URL)
SLACK_WEBHOOK_URL="url"

# Set a threshold for incorrect password attempts
THRESHOLD=3

# Temporary file to track failed login attempts
FAILED_ATTEMPTS_FILE="failed_attempts.log"

# Function to send alert to Slack
send_alert_to_slack() {
  local username=$1
  local message="*ALERT*: User $username has failed to log in 3 times."

  # Send a POST request to Slack with the message
  curl -X POST -H 'Content-type: application/json' \
  --data "{\"text\":\"$message\"}" \
  $SLACK_WEBHOOK_URL
}

# Function to check failed login attempts
check_failed_attempts() {
  local username=$1
  local count=$(grep -o "$username" "$FAILED_ATTEMPTS_FILE" | wc -l)

  if [[ $count -ge $THRESHOLD ]]; then
    send_alert_to_slack "$username"
    # Reset failed attempts after sending the alert
    sed -i "/$username/d" "$FAILED_ATTEMPTS_FILE"
  fi
}

# Function to log failed attempts
log_failed_attempt() {
  local username=$1

  # Log the failed attempt to the temporary file
  echo "$username" >> "$FAILED_ATTEMPTS_FILE"
}

# Monitor the log file for failed login attempts
tail -F $LOG_FILE | while read line; do
  # Check if the line contains "Incorrect password" and extract the email
  if echo "$line" | grep -q "WARNING: Incorrect password for email:"; then
    # Extract the email (adjust this based on your log format)
    username=$(echo $line | grep -oP 'email: \K[^ ]+')

    # Log the failed attempt
    log_failed_attempt "$username"

    # Check if the user has failed 3 times
    check_failed_attempts "$username"
  fi
done
