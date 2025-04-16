## Build with Tenstorrent on Koyeb

This repository serves as a starting point for using on-demand Tenstorrent instances on Koyeb.

Tenstorrent instances are currently available in private preview. You can request access [here](https://www.koyeb.com/tenstorrent).

## Getting started

### Requirements

To deploy your first service using Tenstorrent instances on Koyeb, you need:

- [A Koyeb account](https://app.koyeb.com/auth/signup).
- Access to the private preview for Tenstorrent instances. You can request access [here](https://www.koyeb.com/tenstorrent).

#### [Development Environment with VSCode Integration](https://github.com/koyeb/tenstorrent-examples/tree/main/tt-vsc-tunnel)

Using this one-click application, you will be able to connect a Wormhole instance and establish a connection from your VSCode editor to Koyeb.

_This application is using the official `ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-22.04-amd64-release:latest-rc` Docker image with Docker pre-installed._

#### [Development Environment using Tailscale for SSH access](https://github.com/koyeb/tenstorrent-examples/tree/main/tt-tailscale-ssh)

Using this one-click application, you will be able to get direct SSH access to the Tenstorrent instance using Tailscale.

_This application is using the official `ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-22.04-amd64-release:latest-rc` Docker image with Docker pre-installed._

#### [One-click models](https://github.com/koyeb/tenstorrent-examples/tree/main/tt-models)

Using one of these one-click models, you will be able to deploy a vLLM inference server serving a model on a Tenstorrent instance.
