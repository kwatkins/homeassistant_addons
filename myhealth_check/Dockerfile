ARG BUILD_FROM=ghcr.io/hassio-addons/base:13.2.0
FROM ${BUILD_FROM}

RUN apk add --no-cache python3

WORKDIR /data

COPY run.sh /
COPY server.py /
RUN chmod +x /run.sh /server.py

COPY rootfs/ /

