FROM python:3.11.8-slim-bookworm

COPY src.python.layout-zipapp/layout_zipapp.pex /opt/app/layout_zipapp.pex

ENTRYPOINT ["/bin/bash", "-c", "/opt/app/layout_zipapp.pex"]
