#!/bin/bash

# Check if a filename is provided as a command-line argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename="$1"

# Run the server using the provided filename (replace with the actual command)
python "$filename"

# You can replace the above line with appropriate commands based on your system
# For example, if you're using Flask, you might use "flask run"
# If you're using Node.js, you might use "node server.js"
# Adjust the command to start your server accordingly

