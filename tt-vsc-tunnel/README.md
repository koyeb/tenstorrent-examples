## How to Deploy

Below is an explanation of how to connect directly to a Koyeb Tenstorrent instance through VSCode.

By following this guide, you will be able to deploy a Koyeb service on a Tenstorrent instance and establish a connection from the Koyeb service to your VSCode editor.

### Requirements

To use this example, you need:

- [A Koyeb account](https://app.koyeb.com/auth/signup).
- Access to the private preview for Tenstorrent instances. You can request access [here](https://www.koyeb.com/tenstorrent).
- VSCode installed on your local machine. You can download it from the [official website](https://code.visualstudio.com/).

### Deploy to Koyeb

Get started by creating the service on Koyeb by clicking the button below:

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-vsc-tunnel&type=docker&image=koyeb%2Ftt-vsc-tunnel&privileged=true&service_type=worker&instance_type=gpu-tenstorrent-n300s&regions=was)

### Configuring VSCode for Remote Development

To connect your VSCode editor to the Koyeb service, follow the instructions displayed in the logs once the first deployment is healthy.

```
....
*
* Visual Studio Code Server
*
* By using the software, you agree to
* the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license) and
* the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).
*
[2024-11-07 14:52:49] info Using GitHub for authentication, run `code tunnel user login --provider <provider>` option to change this.
To grant access to the server, please log into https://github.com/login/device and use code C98F-F1F6
...
```

1. Go to [https://github.com/login/device](https://github.com/login/device).
2. Register the service by entering the code displayed in the logs.

_This operation is required after every redeployment but can be avoided by using a Volume to persist the data._

### Connect VSCode to the Koyeb Service

> Ensure you have the [Remote - Tunnels](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-server) extension installed.

On your machine, open VSCode and press `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows/Linux) to open the command palette.

Run the command **"Connect to Tunnel..."**, then choose **GitHub** as the account type to start the tunnel.  
Your Koyeb service will appear in the list of available devices. Select it to instantiate a VSCode instance running on the remote Koyeb service.
