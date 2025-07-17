ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk add --no-cache python3

#WORKDIR /data

COPY run.sh /
COPY server.py /
COPY rootfs/ /

RUN chmod +x /run.sh /server.py



