#!/bin/bash
# Sends a GET request toa given URL with a header variable
curl -sH "X-School-User-Id: 98" "${1}"
