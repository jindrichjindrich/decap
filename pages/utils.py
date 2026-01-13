import yaml

def parse_yaml_context(yaml_text):
    if not yaml_text:
        return {}

    data = yaml.safe_load(yaml_text)

    if data is None:
        return {}

    if not isinstance(data, dict):
        raise ValueError("YAML content must be a mapping (key: value pairs)")

    return data