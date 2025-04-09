## How to Use

Below is a list of one-click models you can use to deploy a Tenstorrent instance on Koyeb.

By following this guide, you will be able to get a running vLLM inference server to serve a model on a Tenstorrent instance.

### Requirements

To deploy one of these one-click models on Koyeb, you need:

- A Koyeb account. If you don't already have an account, you can [sign-up for free](https://app.koyeb.com/auth/signup).
- Access to Tenstorrent instances.

### Deploy to Koyeb

**deepseek-ai/DeepSeek-R1-Distill-Llama-8B**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-deepseek-ai-deepseek-r1-distill-llama-8b&type=docker&image=koyeb%2Ftt-deepseek-ai-deepseek-r1-distill-llama-8b&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=0&env%5BLLAMA_DIR%5D=%2Fmodels%2FDeepSeek-R1-Distill-Llama-8B&hc_grace_period%5B8000%5D=296)

```python
import os

from openai import OpenAI

client = OpenAI(
  api_key = os.environ.get("OPENAI_API_KEY", "fake"),
  base_url="https://<YOUR_DOMAIN_PREFIX>.koyeb.app/v1",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me a joke.",
        }
    ],
    model="/models/DeepSeek-R1-Distill-Llama-8B",
    max_tokens=30,
)

print(chat_completion.to_json(indent=4))
```
