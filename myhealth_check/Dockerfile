ARG BUILD_FROM
FROM $BUILD_FROM


# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3

WORKDIR /data


# Copy data for add-on
COPY run.sh /
COPY server.py /
RUN chmod a+x /run.sh
RUN chmod a+x /server.py

CMD [ "/run.sh" ]
