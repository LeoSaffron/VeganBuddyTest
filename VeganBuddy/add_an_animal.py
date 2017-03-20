#!/usr/bin/python

import json


def read_all_list(filename):
	json_data = open(filename)
	result_list = json.load(json_data)
	return result_list


my_exit_code = 0

name = "test_sounds.json"
mylist = read_all_list(name)
#first = "llama"
#second = "flichen"
#new_item = { first : [second] }
#print json.dumps(mylist)
print mylist
#print new_item
first_variable_name = "animal"
second_variable_name = "food"
print "Enter a %s: " % ( first_variable_name )
first_variable_value = raw_input()
print "Enter a %s: " % ( second_variable_name )
second_variable_value = raw_input()

if first_variable_value in mylist:
	print "There is already %s item is collection of %ss." % (first_variable_value, first_variable_name)
	my_exit_code = 1
else:
	new_item = { first_variable_value : [ second_variable_value ]}
	mylist.update(new_item)
print mylist
with open(name, 'w') as outputfile:
	json.dump(mylist, outputfile)
if my_exit_code == 0:
	print "value has been updated successfully."


