FROM gcc:13-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1001 sandbox
USER sandbox
WORKDIR /sandbox
