import os
import pyodbc
from flask import Flask,render_template,request,url_for,redirect
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
conn_str = os.environ.get("CONN_STR")
port = os.environ.get("PORT", "5000")

app = Flask(__name__)

conn = pyodbc.connect(conn_str)


with conn.cursor() as cursor:
    cursor.execute("SELECT TOP (10) * FROM [SalesLT].[Address]")
    row = cursor.fetchall()
    df = pd.DataFrame()
    for x in row:
        df2 = pd.DataFrame(list(x)).T
        df = pd.concat([df, df2])
    df.to_html('templates/sql-data.html')

