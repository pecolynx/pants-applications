FROM python:3.10.14-slim-bookworm

WORKDIR /opt/app

COPY src.python.grpc-server/grpc_server.pex /opt/app/grpc_server.pex

ENTRYPOINT ["/bin/bash", "-c", "/opt/app/grpc_server.pex"]
