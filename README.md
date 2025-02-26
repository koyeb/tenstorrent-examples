## Build with Tenstorrent on Koyeb

This repository serves as a starting point for using on-demand Tenstorrent instances on Koyeb.

Tenstorrent instances are currently available in private preview. You can request access [here](https://www.koyeb.com/tenstorrent).

## Getting started

### Requirements

To deploy your first service using Tenstorrent instances on Koyeb, you need:

- [A Koyeb account](https://app.koyeb.com/auth/signup).
- Access to the private preview for Tenstorrent instances. You can request access [here](https://www.koyeb.com/tenstorrent).
- [The Koyeb CLI](https://www.koyeb.com/docs/build-and-deploy/cli/installation) installed on your machine to connect the Tenstorrent service.

### Deploy your first service on Tenstorrent

The fastest way to get started and access a Tenstorrent instance is to use the pre-built one-click deployment button below:

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-metalium-ubuntu-20-04-amd64-release&type=docker&image=ghcr.io%2Ftenstorrent%2Ftt-metal%2Ftt-metalium-ubuntu-20.04-amd64-release%3Alatest-rc&entrypoint=sleep&entrypoint=infinity&privileged=true&service_type=worker&instance_type=gpu-tenstorrent-n300s&regions=was)

This service will be deployed on a Tenstorrent instance with a ready-to-use environment, including Tenstorrent system tools and drivers, [TT-Metalium](https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/index.html), and [TT-NN](https://docs.tenstorrent.com/tt-metal/latest/ttnn/index.html) installed using the official `ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-20.04-amd64-release:latest-rc` Docker image.

### Connect to your Tenstorrent instance

When your service is deployed, you can connect to your Tenstorrent instance using the Koyeb CLI.

To connect to the Tenstorrent instance, use the [Koyeb CLI](https://docs.koyeb.com/docs/cli/installation) and execute the following command:

```bash
koyeb service exec <YOUR_KOYEB_APP_NAME>/<YOUR_KOYEB_SERVICE_NAME> /bin/bash
```

_Make sure to replace `<YOUR_KOYEB_APP_NAME>` and `<YOUR_KOYEB_SERVICE_NAME>` with your actual Koyeb app and service names._

Once you're connected, run the following command to execute an example and verify that everything is working as expected:

```bash
python3 -m ttnn.examples.usage.run_op_on_device
```

You are all set! Visit the [TT-NN Basic examples page](https://docs.tenstorrent.com/tt-metal/latest/ttnn/ttnn/usage.html#basic-examples) or get started with [simple kernels on TT-Metalium](https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/examples/index.html).

### Other options

#### [Development Environment with VSCode Integration](https://github.com/koyeb/tenstorrent-examples/tree/main/tt-vsc-tunnel)

Using this one-click application, you will be able to connect a Wormhole instance and establish a connection from your VSCode editor to Koyeb.

_This application is using the official `ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-20.04-amd64-release:latest-rc` Docker image with Docker pre-installed._

#### [Development Environment using Tailscale for SSH access](https://github.com/koyeb/tenstorrent-examples/tree/main/tt-tailscale-ssh)

Using this one-click application, you will be able to get direct SSH access to the Tenstorrent instance using Tailscale.

_This application is using the official `ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-20.04-amd64-release:latest-rc` Docker image with Docker pre-installed._
