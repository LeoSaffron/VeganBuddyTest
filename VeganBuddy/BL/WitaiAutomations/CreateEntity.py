import httplib
import urllib


WIT_API_URL = "api.wit.ai/entities?v=20170403&q="
CONF_FILE_PATH = "Configurations/JSON_files/general_configurations.json"

class CreateEntity(object):
    """
    A Class for Creating an entity.
    """
    def __init__(self):
        self.general_configurations = JSONConfigurationReader().read_json_configuration(CONF_FILE_PATH)
        #self.CONST_UNKNOWN_DICT_FOR_URLLIB = {'@number': 12524, '@type': 'issue', '@action': 'show'}

    def create_entity(self):
        params_dict = '{"doc":"Test", "id":"new_entity_tst", "values":[{"value":"Name of Test Entity",' \
                      '"expressions":["Name of Entity", "Entity Name"]}]}'

        headers = {"Content-type": "application/json",
                   "Authorization": "Bearer {0}".format(self.general_configurations['access_token2'])}
        conn = httplib.HTTPSConnection(WIT_API_URL)
        conn.request("POST", "", urllib.urlencode(params_dict), headers)
        response = conn.getresponse()
        print response.status, response.reason
        print response.read()
        conn.close()

