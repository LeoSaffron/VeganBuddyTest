from Main import *
from BL.WitaiAutomations.CreateEntity import *


def create_entity():
    create_entity_obj = CreateEntity(JSONConfigurationReader().read_json_configuration(CONF_FILE_PATH))
    create_entity_obj.create_entity()


create_entity()
