FROM python:3.8-alpine AS suricataindex

LABEL maintainer="Wyatt Roersma wyatt@aucr.io"
COPY requirements.txt /tmp/
COPY ./suricataindex /tmp/suricataindex
COPY setup.py /tmp/
RUN  apk update && apk upgrade && apk add --no-cache \
    gcc \
    libc-dev \
    musl-dev \
    linux-headers \
    libffi-dev \
    py-pillow \
    python3-dev \
    openssl \
    file \
    jansson \
    bison \
    tini \
    su-exec \
    g++ \
    lapack-dev \
    gfortran \
    build-base \
    suricata \
  && suricata-update update-sources \
  &&  suricata-update enable-source tgreen/hunting  \
  &&  suricata-update enable-source etnetera/aggressive  \
  &&  suricata-update enable-source sslbl/ssl-fp-blacklist  \
  &&  suricata-update enable-source ptresearch/attackdetection  \
  &&  suricata-update enable-source oisf/trafficid \
  &&  suricata-update enable-source et/open \
  && suricata-update \
  && mkdir /opt/suricataindex \
  && pip install -r /tmp/requirements.txt \
  && cd /tmp/ \
  && python setup.py install \
  && mkdir /opt/output/ \
  && mkdir /opt/pcaps/ \
  && apk del --purge gcc \
    libc-dev \
    musl-dev \
    linux-headers \
    libffi-dev \
    py-pillow \
    python3-dev \
    openssl \
    file \
    jansson \
    bison \
    tini \
    su-exec \
    g++ \
    lapack-dev \
    gfortran \
    build-base

WORKDIR /opt/suricataindex/
