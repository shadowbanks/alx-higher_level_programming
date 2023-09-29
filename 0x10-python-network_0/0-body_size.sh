#!/usr/bin/bash
# Get the body size (byte) of a response
curl -sI $@ | grep Content-Length | grep -Eo '[0-9]+'
