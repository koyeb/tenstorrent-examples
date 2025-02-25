#!/bin/sh

_term() {
    echo "Caught SIGTERM signal. Logging out and cleaning up."
    trap - TERM
    kill -TERM $TAILSCALE_DAEMON_PID
    wait $TAILSCALE_DAEMON_PID
}

trap _term TERM

/workdir/tailscaled --state=/var/lib/tailscale/tailscaled.state --socket=/var/run/tailscale/tailscaled.sock &
TAILSCALE_DAEMON_PID=$!
/workdir/tailscale up --ssh --authkey=${TAILSCALE_AUTHKEY} --hostname=${NODE_NAME:-tt-on-koyeb}

wait
