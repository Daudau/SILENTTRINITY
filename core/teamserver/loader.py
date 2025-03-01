import os
import logging
from importlib import util as importlib

class Loader:
    def __init__(self, type="module", paths=[]):
        self.type = type
        self.paths = paths
        self.loaded = []

        self.get_loadables()

    def is_sane(self, module):
        return True

    def load(self, path):
        module_spec = importlib.spec_from_file_location(self.type, path)
        module = importlib.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        self.is_sane(module)
        return module

    def get_loadables(self):
        self.loaded = []
        for path in self.paths:
            for module in os.listdir(path):
                if module[-3:] == '.py' and not module.startswith("example"):
                    try:
                        m = self.load(os.path.join(path, module))
                        if self.type == 'listener':
                            self.loaded.append(m.STListener())
                        elif self.type == 'module':
                            self.loaded.append(m.STModule())
                        elif self.type == 'stager':
                            self.loaded.append(m.STStager())
                        elif self.type == 'server':
                            self.loaded.append(m.STServer())
                    except Exception as e:
                        logging.error(f'Failed loading {self.type} {os.path.join(path, module)}: {e}')

        logging.debug(f"Loaded {len(self.loaded)} {self.type}(s)")
        return self.loaded
