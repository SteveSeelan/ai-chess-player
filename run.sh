#!/bin/bash

# --- Configuration ---
# Name of your Python file containing the FastAPI app instance (e.g., app = FastAPI())
PYTHON_APP_FILE="src.main"
# Name of your FastAPI app instance (e.g., app = FastAPI())
FASTAPI_APP_INSTANCE="app"
# Host to bind to (0.0.0.0 for local network access)
HOST="0.0.0.0"
# Port to listen on
PORT="8765"
# Name of your virtual environment directory
VENV_DIR=".venv"
# Path to your requirements.txt file (if you have one)
REQUIREMENTS_FILE="requirements.txt"

# --- Functions ---

# Function to create and activate a virtual environment
setup_venv() {
    if [ -d "$VENV_DIR" ]; then
        echo "Virtual environment '$VENV_DIR' already exists. Activating..."
    else
        echo "Creating virtual environment '$VENV_DIR'..."
        python3 -m venv "$VENV_DIR" --system-site-packages
        if [ $? -ne 0 ]; then
            echo "Error: Failed to create virtual environment. Exiting."
            exit 1
        fi
    fi
    source "$VENV_DIR/bin/activate"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to activate virtual environment. Exiting."
        exit 1
    fi
    echo "Virtual environment activated."
}

# Function to install dependencies
install_dependencies() {
    if [ -f "$REQUIREMENTS_FILE" ]; then
        echo "Installing dependencies from $REQUIREMENTS_FILE..."
        pip install --upgrade pip
        pip install -r "$REQUIREMENTS_FILE"
        if [ $? -ne 0 ]; then
            echo "Error: Failed to install Python dependencies. Exiting."
            exit 1
        fi
        echo "Dependencies installed."
    else
        echo "No $REQUIREMENTS_FILE found. Skipping dependency installation."
        echo "Please ensure 'uvicorn' and 'fastapi' are installed globally or create a requirements.txt file."
        # Attempt to install if not explicitly handled by requirements.txt
        pip install uvicorn fastapi
    fi
}

# Function to start the FastAPI server
start_fastapi() {
    echo "Starting FastAPI server on http://$HOST:$PORT with auto-reload..."
    # The --reload flag should generally only be used for development.
    # For production, you'd remove --reload and potentially use a process manager like Gunicorn.
    python3 -m uvicorn "$PYTHON_APP_FILE:$FASTAPI_APP_INSTANCE" --host "$HOST" --port "$PORT" --reload
}

# --- Main Script Execution ---

# 1. Set up and activate the virtual environment
setup_venv

# 2. Install dependencies (including uvicorn and fastapi)
install_dependencies

# 3. Start the FastAPI server
start_fastapi

# Deactivate virtual environment when the script exits
deactivate
echo "Server stopped and virtual environment deactivated."