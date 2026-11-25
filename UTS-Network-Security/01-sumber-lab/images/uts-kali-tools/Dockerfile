FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install -y --no-install-recommends \
    aircrack-ng \
    dsniff \
    net-tools \
    iproute2 \
    iputils-ping \
    procps \
    python3 \
    python3-scapy \
    hping3 \
    tcpdump \
    curl \
    dnsutils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["sleep", "infinity"]