#!/usr/bin/python
"""
    The main module for the VeganBuddy bot.
    This is where it starts, and gets its actions defined.
"""
import sys
import json
from wit import Wit
from BL.NutritionValues.NutritionValues import *


class BotActions(object):
    """
    An object of a veganBuddy bot.
    """
    def __init__(self, access_token):
        self.access_token = access_token
        self.actions = {
            'send': self.send,
            'get_nutrition_value': NutritionValues.get_nutrition_value,
            #'get_animal_eat': class_name.get_animal_eat,
            #'get_protein_amount_by_food': get_protein_amount_by_food
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


def main(access_token):
    facebook_bot = BotActions(access_token)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print 'usage: python ' + sys.argv[0] + ' <config-file>'
        exit(1)
    elif len(sys.argv) == 1:
        print "Trying to get default config file"
        with open("Configurations/config.json") as json_conf_file:
            CONF = json.load(json_conf_file)
        ACCESS_TOKEN = CONF['access_token']
        print "TOKEN: %s" % ACCESS_TOKEN
        main(ACCESS_TOKEN)
    else:
        print "Using access_token from %s" % sys.argv[1]
        with open(sys.argv[1]) as json_conf_file:
            CONF = json.load(json_conf_file)
        ACCESS_TOKEN = CONF['access_token']
        print "TOKEN: %s" % ACCESS_TOKEN
        main(ACCESS_TOKEN)
