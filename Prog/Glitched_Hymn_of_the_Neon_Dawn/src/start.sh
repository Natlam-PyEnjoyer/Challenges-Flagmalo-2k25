#!/bin/bash
docker build -t neon-hymn:latest .
docker run -d -p 9000:9000 neon-hymn:latest
