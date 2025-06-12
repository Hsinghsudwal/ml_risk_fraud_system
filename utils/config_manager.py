import yaml
import json
from utils.logger import logger


class ConfigManager:
    def __init__(self, config_dict=None):
        self.config_dict = config_dict or {}
        # Use the singleton logger instance
        # self.logger = logger
        # self.logger.info("ConfigManager initialized")

    def get(self, key, default=None):
        value = self.config_dict.get(key, default)
        logger.debug(f"Retrieved config key '{key}' with value: {value}")
        return value

    @staticmethod
    def load_file(config_file: str):
        """Loads configuration from a YAML or JSON file."""
        try:
            with open(config_file, "r") as file:
                if config_file.endswith((".yml", ".yaml")):
                    config_data = yaml.safe_load(file)
                    # logger.info(f"Loaded YAML config from {config_file}")
                else:
                    config_data = json.load(file)
                    # logger.info(f"Loaded JSON config from {config_file}")
            return ConfigManager(config_data)
        except FileNotFoundError:
            logger.error(f"Config file not found: {config_file}")
            raise ValueError(f"Config file not found: {config_file}")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file {config_file}: {e}")
            raise ValueError(f"Invalid JSON in config file {config_file}: {e}")
        except yaml.YAMLError as e:
            logger.error(f"Invalid YAML in config file {config_file}: {e}")
            raise ValueError(f"Invalid YAML in config file {config_file}: {e}")
