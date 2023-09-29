#!/bin/bash
# List all HTTP methods avaliable
curl -sI 0.0.0.0:5000/route_4 | grep 'Allow' | sed 's/Allow: //'
