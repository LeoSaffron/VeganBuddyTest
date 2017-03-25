import json


class JSONConfigurationReader(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_json_configuration(self):
        with open(self.file_path) as json_conf_file:
            return json.load(json_conf_file)
