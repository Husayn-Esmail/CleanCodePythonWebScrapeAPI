#!/bin/bash
# This script stars the FastAPI server
# export UVICORN_PORT=5000 # set port to 5000
# default host and port is 127.0.0.1:8080
uvicorn main:app --host 0.0.0.0 --reload
