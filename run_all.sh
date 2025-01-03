
#!/bin/bash

# Exit on any error
set -e

# Function to print a header message
print_header() {
    echo "==================================="
    echo "$1"
    echo "==================================="
}

# Step 1: Check Python Installation
print_header "Checking Python Installation"
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Step 2: Set Up Virtual Environment
print_header "Setting Up Python Virtual Environment"
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/Scripts/activate

# Step 3: Install Dependencies
print_header "Installing Dependencies"
#pip install --upgrade pip
pip install -r requirements.txt

print_header "Installing Custom Library: MessageQueue"
pip install ./mypythonlib

# Step 4: Start the Services
print_header "Starting Services"

# Start service_publish
echo "Starting service_publish..."
python ./services/service_publish/main.py > logs/service_publish.log 2>&1 &
PUBLISH_PID=$!
echo "service_publish running with PID $PUBLISH_PID"

# Start service_subscribe
echo "Starting service_subscribe..."
python ./services/service_subscribe/main.py > logs/service_subscribe.log 2>&1 &
SUBSCRIBE_PID=$!
echo "service_subscribe running with PID $SUBSCRIBE_PID"

# Wait for a few seconds to let services initialize
sleep 5

# Step 5: Verify Services
print_header "Verifying Services"
if curl -s http://127.0.0.1:8001 &>/dev/null; then
    echo "service_publish is running successfully."
else
    echo "Error: service_publish is not responding."
fi

if curl -s http://127.0.0.1:8002 &>/dev/null; then
    echo "service_subscribe is running successfully."
else
    echo "Error: service_subscribe is not responding."
fi

# Step 6: Instructions to Stop Services
print_header "All Services Started"
echo "To stop the services, use the following commands:"
echo "kill $PUBLISH_PID  # Stop service_publish"
echo "kill $SUBSCRIBE_PID  # Stop service_subscribe"











