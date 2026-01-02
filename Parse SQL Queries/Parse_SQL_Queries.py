import sys
import math

sql_query = input()
rows = int(input())
table_header = input()

sql_query = sql_query.split()
table_header = table_header.split()

def colums_extract(sql_query):
    colums = []
    for colum in sql_query:
        if colum != 'SELECT':
            colum = colum.replace(',', '')
            colums.append(colum)
        if colum == 'FROM':
            colums.remove(colum)
            break
    return colums

def condition_extract(sql_query):
    state = False
    condition = []
    for word in sql_query:
        if word == 'WHERE':
            state = True
        if state and word != 'WHERE':
            condition.append(word)
        if state and word == 'ORDER':
            condition.remove('ORDER')
            break
    return condition

def order_extract(sql_query):
    state = False
    order = []
    for word in sql_query:
        if word == 'BY':
            state = True
        if state and word != 'BY':
            order.append(word)
    return order

table = []

for i in range(rows):
    table_row = input()
    table_row = table_row.split()
    table.append(table_row)

colums = colums_extract(sql_query)

table_select = []
if condition_extract(sql_query):
    selected_word = condition_extract(sql_query)[-1]
    for row in table:
        if selected_word in row:
            table_select.append(row)
else:
    table_select = table

if order_extract(sql_query):
    field_to_order = order_extract(sql_query)[0]
    sort_type = order_extract(sql_query)[1]
    index_order = table_header.index(field_to_order)
    if type(field_to_order) == int:
        field_to_order = int(field_to_order)
    if sort_type == 'ASC':
        table_order = sorted(table_select, key=lambda x: float(x[index_order]))
    if sort_type == 'DESC':
        table_order = sorted(table_select, key=lambda x: float(x[index_order]), reverse=True)
else:
    table_order = table_select

if colums[0] == '*':
    table_colum = table_order
    table_header_colum = table_header
else:
    index_list = [table_header.index(item) for item in colums if item in table_header]
    table_header_colum = [item for item in colums if item in table_header]
    table_colum = [[row[i] for i in index_list] for row in table_order]

print(*table_header_colum)
for row in table_colum:
    print(*row)




