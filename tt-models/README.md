## How to Use

Below is a list of one-click models you can use to deploy a Tenstorrent instance on Koyeb.

By deploying one of these one-click models, you will be able to get a running vLLM inference server serving a model on a Tenstorrent instance.

Model weights are directly bundled in the container image for each one-click model to provide a better experience with scale-to-zero and autoscaling, avoiding the need to redownload the weights on each newly created instance.

We use [`tt-transformers`](https://github.com/tenstorrent/tt-metal/tree/main/models/tt_transformers) to access and deploy models directly from Hugging Face.

At the time of this writing, the following architectures are known to work:

- LlamaForCausalLM
- Qwen2ForCausalLM
- MistralForCausalLM
- Phi3ForCausalLM

### Requirements

To deploy one of these one-click models on Koyeb, you need:

- [A Koyeb account](https://app.koyeb.com/auth/signup).
- Access to the private preview for Tenstorrent instances. You can request access [here](https://www.koyeb.com/tenstorrent).

### Deploy to Koyeb

**deepseek-ai/DeepSeek-R1-Distill-Llama-8B**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-deepseek-ai-deepseek-r1-distill-llama-8b&type=docker&image=koyeb%2Ftt-deepseek-ai-deepseek-r1-distill-llama-8b&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=0&env%5BLLAMA_DIR%5D=%2Fmodels%2FDeepSeek-R1-Distill-Llama-8B&hc_grace_period%5B8000%5D=600)

**meta-llama/Llama-3.1-8B-Instruct**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-meta-llama-3-1-8b-instruct&type=docker&image=koyeb%2Ftt-meta-llama-3.1-8b-instruct&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=0&hc_grace_period%5B8000%5D=600&entrypoint=python&entrypoint=examples/docker-entrypoint.py&entrypoint=--model&entrypoint=meta-llama/Llama-3.1-8B-Instruct&entrypoint=--tool-call-parser&entrypoint=llama3_json&entrypoint=--chat-template&entrypoint=examples/tool_chat_template_llama3.1_json.jinja&entrypoint=--enable-auto-tool-choice)

**Qwen/Qwen2.5-7B-Instruct**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-qwen-qwen-2-5-7b-instruct&type=docker&image=koyeb%2Ftt-qwen-qwen2.5-7b-instruct&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=0&hc_grace_period%5B8000%5D=600&env[VLLM_ALLOW_LONG_MAX_MODEL_LEN]=1&entrypoint=python&entrypoint=examples/docker-entrypoint.py&entrypoint=--model&entrypoint=Qwen/Qwen2.5-7B-Instruct&entrypoint=--tool-call-parser&entrypoint=hermes&entrypoint=--enable-auto-tool-choice)

**meta-llama/Llama-3.2-3B-Instruct**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-meta-llama-3-2-3b-instruct&type=docker&image=koyeb%2Ftt-meta-llama-3.2-3b-instruct&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=0&hc_grace_period%5B8000%5D=600&entrypoint=python&entrypoint=examples/docker-entrypoint.py&entrypoint=--model&entrypoint=meta-llama/Llama-3.2-3B-Instruct&entrypoint=--tool-call-parser&entrypoint=llama3_json&entrypoint=--chat-template&entrypoint=examples/tool_chat_template_llama3.2_json.jinja&entrypoint=--enable-auto-tool-choice)

**meta-llama/Llama-3.2-1B-Instruct**

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=tt-meta-llama-3-2-1b-instruct&type=docker&image=koyeb%2Ftt-meta-llama-3.2-1b-instruct&instance_type=gpu-tenstorrent-n300s&regions=na&instances_min=0&hc_grace_period%5B8000%5D=600&entrypoint=python&entrypoint=examples/docker-entrypoint.py&entrypoint=--model&entrypoint=meta-llama/Llama-3.2-1B-Instruct&entrypoint=--tool-call-parser&entrypoint=llama3_json&entrypoint=--chat-template&entrypoint=examples/tool_chat_template_llama3.2_json.jinja&entrypoint=--enable-auto-tool-choice)

### Usage example

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
    model="meta-llama/Llama-3.1-8B-Instruct",
    max_tokens=30,
)

print(chat_completion.to_json(indent=4))
```
