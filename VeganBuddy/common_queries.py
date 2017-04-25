#!/usr/bin/python
import sys

import db_connection


# ************************************************
# *********     SELECT  FUNCTIONS   **************
# ************************************************

def single_value_select(table, column_needed, condition_column, condition_value):
    db = db_connection.db_connection()
    db.connect()
    cursor = db.query("SELECT " + column_needed + " FROM " + table + " WHERE " +
                      condition_column + "=" + '"' + str(condition_value) + '"')
    rowcount = int(cursor.rowcount)
    for i in range(0, rowcount):
        row = cursor.fetchone()
        return row[0]
    return -1


def get_iron_amount_in_product_by_product_name(product_name):
    product_id = get_product_id_by_name(product_name)
    if product_id == -1:
        return -2
    return single_value_select('iron_per_product', 'value', 'product', product_id)


def get_protein_amount_in_product_by_product_name(product_name):
    product_id = get_product_id_by_name(product_name)
    if product_id == -1:
        return -2
    return single_value_select('protein_per_product', 'value', 'product', product_id)


def get_product_id_by_name(product_name):
    return single_value_select('food_product', 'id', 'name', product_name)

def get_if_product_exists_in_specific_table(table, column_name, product_name):
    product_id = str(get_product_id_by_name(product_name))
    db = db_connection.db_connection()
    db.connect()
    cursor = db.query("SELECT " + column_name + " FROM " + table + " WHERE " +
                      column_name + "=" + '"' + product_id + '"')
    rowcount = int(cursor.rowcount)
    if rowcount > 0:
        return 1
    return 0


# ************************************************
# *********     UPDATE  FUNCTIONS   **************
# ************************************************

def update_protein_amount_by_product_name(product_name, protein_amount):
    table = "protein_per_product"
    column_value = "value"
    value = str(protein_amount)
    product_column = "product"
    product_id = str(get_product_id_by_name(product_name))
    if product_id == -1:
        return -2
    entry_exist_flag = get_if_product_exists_in_specific_table("protein_per_product", product_column, product_name)
    if entry_exist_flag == 0:
        add_protein_amount_by_product_name(product_name, protein_amount)
        return 0
    query = "UPDATE " + table + " SET " + column_value + " = '" + value + "' WHERE " + \
            product_column + " = '" + product_id + "'"
    db = db_connection.db_connection()
    db.connect()
    db.query(query)
    return 0


def add_protein_amount_by_product_name(product_name, protein_amount):
    add_pair_data_entry_single_value_no_dup("protein_per_product", "product", product_name, "value", protein_amount)
    return 0




def add_a_single_product_by_product_name(product_name):
    return add_single_entry_single_value_no_dup("food_product", "name", product_name)


def add_single_entry_single_value_no_dup(table_name, column_name, value):
    # if value == "":
    #     return -3
    if not value:
        return -3
    product_id = get_product_id_by_name(value)
    if product_id != -1:
        return -1
    table = table_name
    column = column_name
    query = "INSERT INTO " + table + " (" + column + ") VALUES ('" + value + "')"
    db = db_connection.db_connection()
    db.connect()
    db.query(query)
    return 0


def add_pair_data_entry_single_value_no_dup(table_name, first_column, first_value, second_column, second_value):
    # if value == "":
    #     return -3
    if not first_value:
        return -3
    product_id = str(get_product_id_by_name(first_value))
    table = table_name
    column = first_column
    query = "INSERT INTO " + table + " (" + first_column + ", " + second_column + \
            ") VALUES ('" + product_id + "', ' " + str(second_value) + "')"
    db = db_connection.db_connection()
    db.connect()
    db.query(query)
    return 0
