#!/bin/bash
# Display the status code
curl -sI -w %{http_code} -o /dev/null $@
