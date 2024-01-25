import psycopg2
from flask import Flask, render_template
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname="Jogos",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

def create(table, **kwargs):
    columns = ', '.join(kwargs.keys())
    values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in kwargs.values()])
    insert_sql = f"INSERT INTO {table} ({columns}) VALUES ({values})"
    cur.execute(insert_sql)
    conn.commit()

def read(table, **kwargs):
    select_sql = f"SELECT * FROM {table}"
    if kwargs:
        conditions = ' AND '.join([f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}" for key, value in kwargs.items()])
        select_sql += f" WHERE {conditions}"
    cur.execute(select_sql)
    return cur.fetchall()

def update(table, id_column, id_value, **kwargs):
    set_values = ', '.join([f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}" for key, value in kwargs.items()])
    update_sql = f"UPDATE {table} SET {set_values} WHERE {id_column} = {id_value}"
    cur.execute(update_sql)
    conn.commit()

def delete(table, id_column, id_value):
    delete_sql = f"DELETE FROM {table} WHERE {id_column} = {id_value}"
    cur.execute(delete_sql)
    conn.commit()

cur = conn.cursor()

def create(table, **kwargs):
    columns = ', '.join(kwargs.keys())
    values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in kwargs.values()])
    insert_sql = f"INSERT INTO {table} ({columns}) VALUES ({values})"
    cur.execute(insert_sql)
    conn.commit()

def read(table, **kwargs):
    select_sql = f"SELECT * FROM {table}"
    if kwargs:
        conditions = ' AND '.join([f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}" for key, value in kwargs.items()])
        select_sql += f" WHERE {conditions}"
    cur.execute(select_sql)
    return cur.fetchall()

def update(table, id_column, id_value, **kwargs):
    set_values = ', '.join([f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}" for key, value in kwargs.items()])
    update_sql = f"UPDATE {table} SET {set_values} WHERE {id_column} = {id_value}"
    cur.execute(update_sql)
    conn.commit()

def delete(table, id_column, id_value):
    delete_sql = f"DELETE FROM {table} WHERE {id_column} = {id_value}"
    cur.execute(delete_sql)
    conn.commit()

