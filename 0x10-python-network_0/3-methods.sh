#!/bin/bash
# List all HTTP methods avaliable
curl -sI $@ | grep 'Allow' | sed 's/Allow: //'
