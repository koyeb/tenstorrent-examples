## How to Deploy

Below is an explanation of how to connect directly to a Koyeb Tenstorrent instance through SSH using Tailscale.

By following this guide, you will be able to deploy a Koyeb service on a Tenstorrent instance and establish a connection from the Koyeb service via SSH.

### Requirements

To use this example, you need:

- [A Koyeb account](https://app.koyeb.com/auth/signup).
- Access to the private preview for Tenstorrent instances. You can request access [here](https://www.koyeb.com/tenstorrent).
- A Tailscale authentication key to authenticate to your Tailscale network. You can generate an appropriate key by signing up for or logging into a [Tailscale account](https://login.tailscale.com/login) and visiting the [keys settings page](https://login.tailscale.com/admin/settings/keys). Create a key with the **Reusable** and **Ephemeral** options selected for use with Koyeb.

### Deploy to Koyeb

Get started by creating the service on Koyeb by clicking the button below:

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-tailscale-ssh&type=docker&image=koyeb%2Ftt-tailscale-ssh&privileged=true&service_type=worker&instance_type=gpu-tenstorrent-n300s&regions=was&env%5BTAILSCALE_AUTHKEY%5D=REPLACE_ME&env%5BNODE_NAME%5D=tt-on-koyeb)

Clicking on this button brings you to the Koyeb Service creation page with the settings pre-configured to launch this application. Make sure to modify the `TAILSCALE_AUTHKEY` environment variable with your own value during the configuration process.

Once the service is deployed, you can SSH into the `root` account of your Koyeb Instance from another machine on your Tailscale network. The Koyeb Instance's Tailscale hostname should have the following format: `tt-on-koyeb`. You can change the hostname by modifying the `NODE_NAME` environment variable.
