"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa9fm7avj5o48fnamg-a.oregon-postgres.render.com",
        database="todo_iuf7",
        user="root",
        password="4eFWG4q5BKUpZF8QTGdr7n6bf1YSqt2b")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
