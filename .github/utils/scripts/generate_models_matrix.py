import json

from workflows.model_spec import MODEL_SPECS, DeviceTypes, ModelStatusTypes

matrix = {"include": []}

for _, model_spec in MODEL_SPECS.items():
    if (
        (
            model_spec.device_type == DeviceTypes.N300
            or model_spec.device_type == DeviceTypes.P150
        )
        and model_spec.device_model_spec.default_impl
        and (
            model_spec.status == ModelStatusTypes.FUNCTIONAL
            or model_spec.status == ModelStatusTypes.EXPERIMENTAL
            or model_spec.status == ModelStatusTypes.COMPLETE
            or model_spec.status == ModelStatusTypes.TOP_PERF
        )
    ):
        model_dict = model_spec.get_serialized_dict()

        # Replace docker image tag from 'release' to 'dev'
        # if "docker_image" in model_dict:
        #     model_dict["docker_image"] = model_dict["docker_image"].replace(
        #         "vllm-tt-metal-src-release", "vllm-tt-metal-src-dev"
        #     )

        matrix["include"].append(model_dict)

print(json.dumps(matrix, indent=2, ensure_ascii=False))
