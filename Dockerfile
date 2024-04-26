FROM ubuntu:24.04
LABEL org.opencontainers.image.source https://github.com/checkmarx-ts/cxone-flow
LABEL org.opencontainers.image.vendor Checkmarx Professional Services
LABEL org.opencontainers.image.title Checkmarx One Flow
LABEL org.opencontainers.image.description Orchestrates scans for Checkmarx One

USER root

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata && \
    apt-get install -y python3.12 python3-pip python3-debugpy bash

    # usermod -s /bin/bash nobody && \
    # mkdir -p /opt/cxone && \
    # mkfifo /opt/cxone/logfifo && \
    # chown nobody:root /opt/cxone/logfifo


# WORKDIR /opt/cxone
# COPY *.txt /opt/cxone

# RUN pip install -r requirements.txt --no-cache-dir --break-system-packages && \
#     apt-get remove -y perl && \
#     apt-get autoremove -y && \
#     apt-get clean && \
#     dpkg --purge $(dpkg --get-selections | grep deinstall | cut -f1)

# COPY cxone_api /opt/cxone/cxone_api
# COPY logic /opt/cxone/logic
# COPY utils /opt/cxone/utils
# COPY *.py /opt/cxone
# COPY entrypoint.sh /opt/cxone
# COPY *.json /opt/cxone


# RUN ln -s scheduler.py scheduler && \
#     ln -s scheduler.py audit

# CMD ["scheduler"]
# ENTRYPOINT ["/opt/cxone/entrypoint.sh"]
