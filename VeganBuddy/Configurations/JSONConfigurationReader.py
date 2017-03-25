import json


class JSONConfigurationReader(object):
    def __init__(self):
        pass

    @staticmethod
    def read_json_configuration(file_path):
        with open(file_path) as json_conf_file:
            return json.load(json_conf_file)
