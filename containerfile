FROM python:3.9-alpine

ARG PHANTOM_BINARY="phantomjs-2.1.1-linux-x86_64.tar.bz2"
ARG GECKO_VERSION="v0.29.1"
ARG GECKO_PACKAGE="geckodriver-${GECKO_VERSION}-linux64.tar.gz"

RUN apk update && \
    apk add \
        curl \
        bzip2 \
        tar \
        firefox-esr

RUN pip install \
    selenium \
    tabulate \
    pyyaml

 RUN curl -sSL \
        https://bitbucket.org/ariya/phantomjs/downloads/${PHANTOM_BINARY} \
        -o ${PHANTOM_BINARY} && \
    bzip2 --decompress ${PHANTOM_BINARY} && \
    tar xvf ${PHANTOM_BINARY%.*} && \
    mv ${PHANTOM_BINARY%.*.*}/bin/phantomjs /usr/bin/ && \
    rm -rf ${PHANTOM_BINARY%.*.*} && \
    rm ${PHANTOM_BINARY%.*}

RUN curl -sSL \
        https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/${GECKO_PACKAGE} \
        -o ${GECKO_PACKAGE} && \
    tar zxvf ${GECKO_PACKAGE} && \
    mv geckodriver /usr/bin/ && \
    rm ${GECKO_PACKAGE}

COPY ./src/main.py /
COPY ./src/stores.yml /

ENTRYPOINT ["python", "main.py"]