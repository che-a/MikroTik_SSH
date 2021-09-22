#!/usr/bin/env bash

# Выполнение консольной команды на MikroTik через SSH

LOGIN=$1
PASSWORD=$2
IP=$3
PORT=$4
CMD=$5

sshpass -p "$PASSWORD" \
    ssh -o 'IdentitiesOnly=yes' \
        -o 'ConnectTimeout=30' \
        -o 'StrictHostKeyChecking=no' \
        -p "$PORT" \
        "$LOGIN"@"$IP" "$CMD"