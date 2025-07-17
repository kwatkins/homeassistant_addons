#!/usr/bin/with-contenv bashio
#!/usr/bin/with-contenv bashio

bashio::log.info "Getting configuration..."
PORT=$(bashio::config 'port')

bashio::log.info "Starting health check on port ${PORT}..."

python3 /server.py
