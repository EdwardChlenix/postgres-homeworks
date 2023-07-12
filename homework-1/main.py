"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

with open('./north_data/employees_data.csv') as f:
    list_of_employees_data = []
    data = csv.reader(f, delimiter=',')
    for line in data:
        list_of_employees_data.append(line)


with open('./north_data/customers_data.csv') as f:
    list_of_customers_data = []
    data = csv.reader(f, delimiter=',')
    for line in data:
        list_of_customers_data.append(line)


with open('./north_data/orders_data.csv', encoding='utf8') as f:
    list_of_orders_data = []
    data = csv.reader(f, delimiter=',')
    for line in data:
        list_of_orders_data.append(line)




with psycopg2.connect(host='localhost', database='north', user='postgres', password='556473') as conn:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', list_of_employees_data[1:])
        cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', list_of_customers_data[1:])
        cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', list_of_orders_data[1:])

