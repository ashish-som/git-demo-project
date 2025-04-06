import yaml

def config_reader(path):
    return yaml.safe_load(path)