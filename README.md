# Build with Tenstorrent on Koyeb

This repository serves as a starting point for using on-demand Tenstorrent instances on Koyeb.

> **Note:** Tenstorrent instances are currently available in private preview. You can request access [here](https://www.koyeb.com/tenstorrent).

## Table of Contents

- [Build with Tenstorrent on Koyeb](#build-with-tenstorrent-on-koyeb)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Requirements](#requirements)
  - [Development Environments](#development-environments)
    - [VSCode Integration](#vscode-integration)
    - [SSH Access via Koyeb TCP Proxy](#ssh-access-via-koyeb-tcp-proxy)
    - [SSH Access via Tailscale](#ssh-access-via-tailscale)
  - [One-Click Model Deployment](#one-click-model-deployment)
    - [Available Models](#available-models)
  - [Usage Examples](#usage-examples)
    - [Python Example](#python-example)
    - [cURL Example](#curl-example)

## Getting Started

### Requirements

To deploy your first service using Tenstorrent instances on Koyeb, you need:

- [A Koyeb account](https://app.koyeb.com/auth/signup)
- Access to the private preview for Tenstorrent instances ([request access](https://www.koyeb.com/tenstorrent))

## Development Environments

### VSCode Integration

Connect your VSCode editor directly to a Tenstorrent instance for seamless development.

**Features:**

- Full VSCode experience running on Tenstorrent hardware
- Direct access to the official TT-Metal development environment
- Persistent development environment with Docker support
- Full root access for custom configurations

[**📖 View detailed setup guide →**](https://github.com/koyeb/tenstorrent-examples/tree/main/tt-vsc-tunnel)

_Uses the official `ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-22.04-release-amd64:latest-rc` Docker image with Docker pre-installed._

### SSH Access via Koyeb TCP Proxy

Get direct SSH access to your Tenstorrent instance using Koyeb TCP Proxy.

**Features:**

- Direct SSH access to your Tenstorrent instance
- Secure connection through Koyeb TCP Proxy
- Full root access for custom configurations

[**📖 View detailed setup guide →**](https://github.com/koyeb/tenstorrent-examples/tree/main/tt-ssh)

_Uses the official `ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-22.04-release-amd64:latest-rc` Docker image with Docker pre-installed._

### SSH Access via Tailscale

Get direct SSH access to your Tenstorrent instance using Tailscale.

**Features:**

- Direct SSH access to your Tenstorrent instance
- Secure connection through Tailscale VPN
- Full root access for custom configurations

[**📖 View detailed setup guide →**](https://github.com/koyeb/tenstorrent-examples/tree/main/tt-tailscale-ssh)

_Uses the official `ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-22.04-release-amd64:latest-rc` Docker image with Docker pre-installed._

## One-Click Model Deployment

Deploy pre-configured AI models optimized for Tenstorrent hardware. Model weights are bundled directly in container images for faster startup and better autoscaling performance.

**Technical Details:**

- Built using [`tt-inference-server`](https://github.com/tenstorrent/tt-inference-server)
- OpenAI-compatible API endpoints
- Automatic model optimization for Tenstorrent hardware

### Available Models

**Meta Llama 3.1 8B Instruct**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-meta-llama-llama-3-1-8b-instruct&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-meta-llama-llama-3.1-8b-instruct&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

**Meta Llama 3.1 8B**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-meta-llama-llama-3-1-8b&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-meta-llama-llama-3.1-8b&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

**Meta Llama 3.2 11B**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-meta-llama-llama-3-2-11b&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-meta-llama-llama-3.2-11b&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

**Meta Llama 3.2 11B Vision Instruct**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-meta-llama-llama-3-2-11b-vision-instruct&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-meta-llama-llama-3.2-11b-vision-instruct&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

**Meta Llama 3.2 11B Vision**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-meta-llama-llama-3-2-11b-vision&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-meta-llama-llama-3.2-11b-vision&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

**Meta Llama 3.2 3B Instruct**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-meta-llama-llama-3-2-3b-instruct&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-meta-llama-llama-3.2-3b-instruct&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

**Meta Llama 3.2 3B**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-meta-llama-llama-3-2-3b&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-meta-llama-llama-3.2-3b&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

**Meta Llama 3.2 1B Instruct**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-meta-llama-llama-3-2-1b-instruct&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-meta-llama-llama-3.2-1b-instruct&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

**Meta Llama 3.2 1B**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-meta-llama-llama-3-2-1b&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-meta-llama-llama-3.2-1b&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

**Arcee AI AFM-4.5B**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-n300-afm-4-5b&type=docker&image=registry01.prod.koyeb.com%2Fkoyeb%2Ftt-n300-arcee-ai-afm-4.5b&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=1&autoscaling_sleep_idle_delay=300&hc_grace_period%5B8000%5D=898)

## Usage Examples

Once the model is deployed, you can interact with it using the OpenAI-compatible API:

### Python Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "fake"),
    base_url="https://<YOUR_DOMAIN_PREFIX>.koyeb.app/v1",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me a joke.",
        }
    ],
    model="meta-llama/Llama-3.1-8B-Instruct",
    max_tokens=30,
)

print(chat_completion.to_json(indent=4))
```

### cURL Example

```bash
curl -X POST "https://<YOUR_DOMAIN_PREFIX>.koyeb.app/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer fake" \
  -d '{
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "messages": [
      {
        "role": "user",
        "content": "Tell me a joke."
      }
    ],
    "max_tokens": 30
  }'
```
