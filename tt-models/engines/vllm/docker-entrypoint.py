import argparse
import runpy
import sys

from offline_inference_tt import check_tt_model_supported, register_tt_models

register_tt_models()  # Import and register models from tt-metal


def parse_args(args):
    result = {}
    it = iter(args)
    for key in it:
        if key.startswith("--"):
            next_item = next(it, None)
            result[key] = (
                None if (next_item is None or next_item.startswith("--")) else next_item
            )
            if (
                result[key] is None
                and next_item is not None
                and not next_item.startswith("--")
            ):
                result[next_item] = None
    return result


def main():
    default_args = {
        "--block_size": "64",
        "--max_num_seqs": "32",
        "--max_model_len": "131072",
        "--max_num_batched_tokens": "131072",
        "--num_scheduler_steps": "10",
    }

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model", type=str, default="meta-llama/Meta-Llama-3.1-70B", help="Model name"
    )
    args, unknown_args = parser.parse_known_args()

    check_tt_model_supported(args.model)

    user_args = parse_args(unknown_args)
    combined_args = {**default_args, **user_args}

    sys.argv = [sys.argv[0], "--model", args.model]
    for k, v in combined_args.items():
        sys.argv.append(k)
        if v is not None:
            sys.argv.append(v)

    runpy.run_module("vllm.entrypoints.openai.api_server", run_name="__main__")


if __name__ == "__main__":
    main()
