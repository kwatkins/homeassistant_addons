#!/usr/bin/with-contenv bashio

bashio::log.info "Getting configuration..."
DEFAULT_PORT=$(bashio::config 'port')

bashio::log.info "Starting health check..."

python3 server.py
