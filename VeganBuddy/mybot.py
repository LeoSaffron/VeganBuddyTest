#!/usr/bin/python
from random import shuffle
import sys
from wit import Wit
import json

#
#if len(sys.argv) != 2:
#	print('usage: python ' + sys.argv[0] + '<wit-token>')
#	exit(1)
#access_token = sys.argv[1]
access_token = "TFIXBQB7NFJ3UVKFOUFUEYCUVXNG64AX"

def send(request, response):
	print (response['text'])
def my_action(request):
	print('Received from user...', request['text'])

def getAnimalEat(request):
	context = request['context']
	entities = request['entities']
	print request
	animal = first_entity_value(entities, 'animal')
	actio = first_entity_value(entities, 'action')
#	print entities['animal'][0]
	random_product=products_by_animals[animal]
#	print entities
#	print animal
#	print actio
	shuffle(random_product)
#	print random_product[0]
	context['food'] = random_product[0]
#	print print_animals_food_single_item()
	return context


def getProteinAmountByFood(request):
	context = request['context']
        entities = request['entities']
        print request
	#protein_amount = protein_amount_per_product[first_entity_value(entities, 'food_product')]
	protein_amount = protein_amount_per_product[most_confident_entity_value(entities, 'food_product')]
	print "protein amount %s" % (protein_amount)
	context['protein_amount'] = protein_amount
	return context


def print_animals_food_single_item():
	result = json.dumps(products_by_animals)
	with open('test_sounds.json','w') as outputfile:
		json.dump(products_by_animals, outputfile)
#	return result

def read_animals_dict_from_json_file(filename):
	json_data = open(filename)
	result_list = json.load(json_data)
	return result_list

def first_entity_value(entities, entity):
	if entity not in entities:
		return None
	val = entities[entity][0]['value']
	if not val:
        	return None
	return val['value'] if isinstance(val, dict) else val

def most_confident_entity_value(entities, entity):
	if entity not in entities:
		return None
	val = entities[entity][0]['value']
	if not val:
        	return None
	confidence = entities[entity][0]['confidence']
	print confidence
	return val['value'] if isinstance(val, dict) else val

actions = {
	'send': send,
#	'my_actions': my_actions,
	'getAnimalEat': getAnimalEat,
	'getProteinAmountByFood' : getProteinAmountByFood
#	'getIronAmountByFood' : getIronAmountByFood
}
#
#products_by_animals = {
#	'fox': [
#		'apples',
#		'blackberries',
#	],
#	'rabbit': [
#		'Carrot',
#		'cabbage',
#	],
#	'cow': [
#		'grass',
#	],
#}

products_by_animals = read_animals_dict_from_json_file("test_sounds.json")
iron_amount_per_product = read_animals_dict_from_json_file("test_iron_by_food_product_amount.json")
protein_amount_per_product = read_animals_dict_from_json_file("test_protein_by_food_product_amount.json")
print products_by_animals 
print iron_amount_per_product
print protein_amount_per_product

#print_animals_food_single_item()
client = Wit(access_token=access_token, actions=actions)
client.interactive()
