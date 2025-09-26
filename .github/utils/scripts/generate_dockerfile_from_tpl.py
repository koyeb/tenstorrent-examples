import argparse
import fnmatch
from pathlib import Path

from huggingface_hub import list_repo_files
from jinja2 import Environment, FileSystemLoader


def model_files_to_download(
    model: str,
    allow_patterns: list[str] = ["*.json", "*.py", "*.safetensors", "*.txt", "*.model"],
):
    files = list_repo_files(model)

    if model == "meta-llama/Llama-3.2-11B-Vision-Instruct":
        allow_patterns.append("original/*")

    filtered_files = [
        file
        for file in files
        if any(fnmatch.fnmatch(file, pattern) for pattern in allow_patterns)
    ]
    return filtered_files


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a Dockefile from a Jinja template to dynamically create layers."
    )
    parser.add_argument(
        "--dockerfile-template",
        type=str,
        required=True,
        help="The Jinja template to use to generate the Dockerfile.",
    )
    parser.add_argument(
        "--dockerfile-output",
        type=str,
        required=True,
        help="The path to write the generated Dockerfile.",
    )
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="The name of the model to download from HuggingFace Hub.",
    )
    parser.add_argument(
        "--allow-patterns",
        type=str,
        nargs="+",
        default=["*.json", "*.py", "*.safetensors", "*.txt", "*.model"],
        help="A list of allowed patterns for snapshot download.",
    )
    parser.add_argument(
        "--base-image",
        type=str,
        required=True,
        help="The base Docker image to use in the Dockerfile.",
    )
    parser.add_argument(
        "--model-spec-json",
        type=str,
        required=True,
        help="The JSON model specification to embed in the Dockerfile.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    files = model_files_to_download(args.model, args.allow_patterns)

    templates_path = Path(__file__).parent.parent / "templates"
    output_file_path = Path(args.dockerfile_output)

    # Create the output directory if it doesn't exist
    output_file_path.parent.mkdir(parents=True, exist_ok=True)

    jinja_env = Environment(loader=FileSystemLoader(str(templates_path)))
    template = jinja_env.get_template(args.dockerfile_template)

    dockerfile_content = template.render(
        hf_model_files=files,
        hf_model=args.model,
        base_image=args.base_image,
        model_spec_json=args.model_spec_json,
    )

    with open(output_file_path, "w") as f:
        f.write(dockerfile_content)


if __name__ == "__main__":
    main()
