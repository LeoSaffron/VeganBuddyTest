import httplib
import urllib


class CreateEntity(object):
    """
    A Class for Creating an entity.
    """
    def __init__(self, general_configuration):
        self.general_configurations = general_configuration

    def create_entity(self):
        params_dict = {"doc": "Test",
                       "id": "new_entity_tst",
                       "values": [{"value": "Name of Test Entity",
                                   "expressions": ["Name of Entity", "Entity Name"]}]}
        headers = {"Authorization": "Bearer {0}".format(self.general_configurations['access_token2'],),
                   "Content-type": "application/json"}

        conn = httplib.HTTPSConnection(self.general_configurations['wit_api_url'])
        conn.request("POST", "entities?v=20170403", urllib.urlencode(params_dict), headers)
        response = conn.getresponse()
        print response.status, response.reason
        print response.read()
        conn.close()
