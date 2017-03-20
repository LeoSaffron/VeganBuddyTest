#!/usr/bin/python
import sys
from wit import Wit


class BotActions(object):
    """
    An object of a veganBuddy bot.
    """
    def __init__(self, access_token):
        self.access_token = access_token
        self.actions = {
            'send': self.send,
            #'get_animal_eat': get_animal_eat,
            #'get_protein_amount_by_food': get_protein_amount_by_food
        }

        self.client = Wit(access_token=self.access_token, actions=self.actions)
        self.client.interactive()

    @staticmethod
    def send(request, response):
        print (response['text'])

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
        print 'usage: python ' + sys.argv[0] + ' <wit-token>'
        exit(1)
    elif len == 1:
        print "Default access token is supplied"
        main()
    else:
        main(sys.argv[1])
