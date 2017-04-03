#!/usr/bin/python
"""
    The main module for the VeganBuddy bot.
    This is where it starts, and gets its actions defined.
"""
import sys
from wit import Wit
from BL.NutritionValues.NutritionValues import *
from Configurations.JSONConfigurationReader import *
import time

CONF_FILE_PATH = "Configurations/JSON_files/general_configurations.json"


class BotActions(object):
    """
    An object of a veganBuddy bot.
    """
    def __init__(self, access_token, general_configurations):
        self.general_configurations = general_configurations
        self.access_token = access_token
        self.actions = {
            'send': self.send,
            'get_nutrition_value': NutritionValues.get_nutrition_value,
        }
        self.client = Wit(access_token=self.access_token, actions=self.actions)
        self.client.interactive()

    @staticmethod
    def send(request, response):
        print response['text']

    @staticmethod
    def first_entity_value(entities, entity):
        if entity not in entities:
            return None
        val = entities[entity][0]['value']
        if not val:
            return None
        return val['value'] if isinstance(val, dict) else val


def main(access_token, general_configurations):
    BotActions(access_token, general_configurations)


def call_main():
    """
    Calling main and ensuring that the user
    entered the right amount of variables.
    """
    if len(sys.argv) > 2:
        print 'usage: python ' + sys.argv[0] + ' <config-file>'
        time.sleep(3)
        exit(1)
    elif len(sys.argv) == 1:
        print "Trying to get default config file"
        general_configurations = JSONConfigurationReader().read_json_configuration(CONF_FILE_PATH)
        ACCESS_TOKEN = general_configurations['access_token']
        print "TOKEN: %s" % ACCESS_TOKEN
        main(ACCESS_TOKEN, general_configurations)
    else:
        print "Using given access_token: ".format(sys.argv[1],)
        main(sys.argv[1])

if __name__ == "__main__":
    call_main()
