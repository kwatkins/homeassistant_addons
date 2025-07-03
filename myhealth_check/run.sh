#!/usr/bin/with-contenv bashio

bashio::log.info "Starting health check..."

python3 server.py
