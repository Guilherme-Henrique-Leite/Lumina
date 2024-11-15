FROM mcr.microsoft.com/devcontainers/base:jammy

RUN mkdir -p /opt/oracle && \
    cd /opt/oracle && \
    wget https://download.oracle.com/otn_software/linux/instantclient/218000/instantclient-basic-linux.x64-21.8.0.0.0dbru.zip && \
    unzip instantclient-basic-linux.x64-21.8.0.0.0dbru.zip && \
    rm instantclient-basic-linux.x64-21.8.0.0.0dbru.zip && \
    sh -c "echo /opt/oracle/instantclient_21_8 > /etc/ld.so.conf.d/oracle-instantclient.conf" && \
    ldconfig && \
    export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_8:$LD_LIBRARY_PATH && \
    apt-get update && \
    apt-get install -y libaio1 vim