#!/usr/bin/env bash

set -euo pipefail

echo $PUBLIC_KEY >/root/.ssh/authorized_keys
chmod 644 /root/.ssh/authorized_keys

/usr/sbin/sshd -D