import json
import os


class ConfigHelper:
    """
    Handles the saving, formatting and loading of the local configuration.
    """
    def __init__(self):
        self._whole_config = {}

    def is_present(self) -> bool:
        return os.path.isfile('config.json')

    def load(self):
        try:
            with open('config.json', 'r') as f:
                config_raw = f.read()
                self._whole_config = json.loads(config_raw)
        except IOError:
            raise ValueError('No config found!')

    def _save(self):
        with open('config.json', 'w+') as f:
            config_formatted = json.dumps(self._whole_config, indent=4)
            f.write(config_formatted)

    def get_property(self, key: str) -> any:
        try:
            return self._whole_config[key]
        except KeyError:
            raise ValueError('The %s-Property is not yet configured!'%(key))

    def set_property(self, key: str, value: any):
        self._whole_config.update({key: value})
        self._save()
