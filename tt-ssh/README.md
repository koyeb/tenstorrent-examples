## How to Deploy

Below is an explanation of how to connect directly to a Koyeb Tenstorrent instance through SSH using [Koyeb TCP Proxy](https://www.koyeb.com/docs/run-and-scale/tcp-proxy).

By following this guide, you will be able to deploy a Koyeb service on a Tenstorrent instance and establish a connection from the Koyeb service via SSH.

### Requirements

To use this example, you need:

- [A Koyeb account](https://app.koyeb.com/auth/signup).
- Access to the private preview for Tenstorrent instances. You can request access [here](https://www.koyeb.com/tenstorrent).
- A public SSH key used to authenticate access to the Koyeb service.

### Deploy to Koyeb

Get started by creating the service on Koyeb by clicking the button below:

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-ssh&type=docker&image=koyeb%2Ftt-ssh&privileged=true&instance_type=gpu-tenstorrent-n300s&regions=na&env%5BPUBLIC_KEY%5D=REPLACE_ME&volume_path%5Btt-data%5D=%2Fworkdir&volume_size%5Btt-data%5D=10&ports=22%3Btcp%3B%3Btrue%3Btcp&instances_min=1)

Clicking on this button brings you to the Koyeb Service creation page with the settings pre-configured to launch this application. Make sure to modify the `PUBLIC_KEY` environment variable with your own value during the configuration process.

After the service is deployed, you can connect to the `root` account of your Koyeb Service via SSH using the Koyeb TCP Proxy details shown in your Koyeb control panel:

```
ssh -p 2222 root@01.proxy.koyeb.app
```

_The command above is an example, make sure to replace the hostname and port with the actual values provided in your Koyeb control panel._
