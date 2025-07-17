ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install requirements for add-on
RUN apk add --no-cache python3

# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
# WORKDIR /data


# Copy data for add-on
COPY run.sh /
COPY server.py /

RUN chmod a+x /run.sh
RUN chmod a+x /server.py
CMD [ "/run.sh" ]
# CMD [ "python3","server.py" ]
