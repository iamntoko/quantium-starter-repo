#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the test suite
python -m pytest tests/

# Capture pytest exit code and propagate it
if [ $? -eq 0 ]; then
    echo "All tests passed!"
else
    echo "Tests failed."
    exit 1
fi