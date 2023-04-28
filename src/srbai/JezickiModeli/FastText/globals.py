import os
from typing import Dict, Any

import yaml


class Config:
    def __init__(self) -> None:
        self.config_dir: str = os.path.join(".", "configs")

    def load_yaml(self, yaml_path: str) -> Dict[str, Any]:
        with open(yaml_path, "rb") as f:
            yaml_data = yaml.safe_load(f)

        return yaml_data


class ModelConfig(Config):
    def __init__(self, model_name: str) -> None:
        super().__init__()

        _yaml_data = self.load_yaml(
            os.path.join(self.config_dir, "models", model_name, "config.yaml")
        )

        _text_preproc = _yaml_data["text_preprocessing"]
        self.ngram_size: int = _text_preproc["ngram_size"]
        self.context_window: Dict[str, int] = _text_preproc["context_window"]
        self.self_context: bool = _text_preproc["self_context"]

        _neural_network = _yaml_data["neural_network"]
        self.vector_space_size: int = _neural_network["vector_space_size"]
        self.optimizer: Dict[str, float] = _neural_network["opti