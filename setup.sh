#!/bin/bash

# Setup script for Deep Learning Course
echo "Setting up Deep Learning Course environment..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "    source venv/bin/activate"
echo ""
echo "To start JupyterLab, run:"
echo "    jupyter-lab"
echo ""
echo "To deactivate the virtual environment, run:"
echo "    deactivate"

