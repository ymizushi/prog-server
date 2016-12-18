import yaml

with open("config.yaml", 'r') as f:
    config = yaml.load(f)
    redis_config = config.get('redis')
    app_config = config.get('app')

