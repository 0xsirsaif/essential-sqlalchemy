"""
1. Run postgresql inside container
    >> docker run
        --name postgresql
        --network=host # To use `localhost` in the connection string.
        -e POSTGRES_USER=saif -e POSTGRES_PASSWORD=mohamed98
        -p 5432:5432
        -v /data:/var/lib/postgresql/data
        -d
        postgres

"""
import datetime

from connection import get_connection
from sqlalchemy import MetaData, Column, Table, Integer, Numeric, String, DateTime, ForeignKey, Boolean


metadata = MetaData()
cookies = Table(
    "cookies",
    metadata,
    Column("cookie_id", Integer(), primary_key=True),
    Column("cookie_name", String(50), index=True),
    Column("cookie_recipe_url", String(255)),
    Column("cookie_sku", String(50)),
    Column("quantity", Integer()),
    Column("unit_cost", Numeric(12, 2)),
)

users = Table(
    "users",
    metadata,
    Column("user_id", Integer(), primary_key=True),
    Column("user_name", String(255), nullable=False),
    Column("email", String(255), nullable=False),
    Column("phone", String(20), nullable=False),
    Column("password", String(20), nullable=False),
    Column("created_on", DateTime(), default=datetime.datetime.now),
    Column("updated_on", DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now),
)

orders = Table(
    "orders",
    metadata,
    Column("order_id", Integer(), primary_key=True),
    Column("user_id", ForeignKey("users.user_id")),
    Column("shipped", Boolean(), default=False),
)

line_items = Table(
    "line_items",
    metadata,
    Column("line_items_id", Integer(), primary_key=True),
    Column("order_id", ForeignKey("orders.order_id")),
    Column("cookie_id", ForeignKey("cookies.cookie_id")),
    Column("quantity", Integer()),
    Column("extended_cost", Numeric(12, 2))
)

engine, connection = get_connection()
metadata.create_all(engine)