FROM alpine:3.11
LABEL maintainer="Noah Altunian <nbaltunian@gmail.com>"

COPY . /mapi
WORKDIR mapi

RUN apk update && \
    apk add --no-cache cargo git make python3 rust

RUN git submodule init && \
    git submodule update &&\
    pip3 install -r requirements.txt && \
    cd mapi.rs && \
    make

CMD ["python3", "mapi/app.py"]

