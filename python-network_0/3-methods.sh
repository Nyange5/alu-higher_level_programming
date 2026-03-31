#!/bin/bash
curl -s -X OPTIONS -i "$1" | grep "Allow:" | cut -d' ' -f2-
