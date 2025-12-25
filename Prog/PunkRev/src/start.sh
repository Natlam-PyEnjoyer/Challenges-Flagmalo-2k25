#!/bin/bash
docker build -t punkrev:latest .
docker run -d -p 9001:9001 punkrev:latest
