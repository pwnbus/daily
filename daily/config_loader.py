import yaml
import os


class ConfigLoader(object):

    def __init__(self, location="../config.yml"):
        config_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), location)
        data = yaml.safe_load(open(config_location))

        self.db_uri = data['db_url']
        self.debug = data['debug']
        self.tasks = data['tasks']
