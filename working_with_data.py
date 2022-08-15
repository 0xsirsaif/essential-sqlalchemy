"""

"""
from main import cookies, line_items, users, orders
from connection import get_connection
from sqlalchemy import insert

connection, engine = get_connection()

# cookie_data = [
#     {
#         "cookie_name": "chocolate chip",
#         "cookie_recipe_url": "http://some.aweso.me/cookie/recipe.html",
#         "cookie_sku": "CC01",
#         "quantity": "12",
#         "unit_cost": "0.50"
#     },
#     {
#         "cookie_name": "chocolate chip",
#         "cookie_recipe_url": "http://some.aweso.me/cookie/recipe.html",
#         "cookie_sku": "CC01",
#         "quantity": "12",
#         "unit_cost": "0.50"
#     }
#
# ]

# INSERT
# ins = cookies.insert()
# result = connection.execute(ins, data)

# customer_list = [
#     {
#         'user_name': 'cookiemon',
#         'email': 'mon@cookie.com',
#         'phone': '111-111-1111',
#         'password': 'password'
#     },
#     {
#         'user_name': 'cakeeater',
#         'email': 'cakeeater@cake.com',
#         'phone': '222-222-2222',
#         'password': 'password'
#     },
#     {
#         'user_name': 'pieguy',
#         'email': 'guy@pie.com',
#         'phone': '333-333-3333',
#         'password': 'password'
#     }
# ]
# ins = users.insert()
# result = connection.execute(ins, customer_list)

# ins = insert(orders).values(user_id=5, order_id=1)
# result = connection.execute(ins)

# ins = insert(line_items)
# order_items = [
#     {
#         'order_id': 1,
#         'cookie_id': 1,
#         'quantity': 2,
#         'extended_cost': 1.00
#     },
#     {
#         'order_id': 1,
#         'cookie_id': 2,
#         'quantity': 12,
#         'extended_cost': 3.00
#     }
# ]
# result = connection.execute(ins, order_items)

# ins = insert(orders).values(user_id=6, order_id=2)
# result = connection.execute(ins)

# ins = insert(line_items)
# order_items = [
#     {
#         'order_id': 2,
#         'cookie_id': 1,
#         'quantity': 24,
#         'extended_cost': 12.00
#     },
#     {
#         'order_id': 2,
#         'cookie_id': 2,
#         'quantity': 6,
#         'extended_cost': 6.00
#     }
# ]
#
# result = connection.execute(ins, order_items)
#

# Query
s = cookies.select()
result_proxy = connection.execute(s)
result = result_proxy.fetchall()
print(result)
