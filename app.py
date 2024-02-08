"""
This app shows how to perform CRUD (Create, Retrieve, Update, Delete) 
operations in Flask web application connected to MS SQL Server.
"""

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


@app.route("/")
def index():
    """Start page of the demo application"""
    return render_template("index.html")


@app.route("/index")
def index_return():
    """Start page of the demo application"""
    return render_template("index.html")


@app.route("/about")
def about():
    """Start page of the demo application"""
    return render_template("about.html")


@app.route("/credits")
def my_credits():
    """Start page of the demo application"""
    return render_template("credits.html")


@app.route("/product_table")
def product_table():

    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP (10) * FROM [SalesLT].[Address]")
        row = cursor.fetchall()
        df = pd.DataFrame()
        for x in row:
            df2 = pd.DataFrame(list(x)).T
            df = pd.concat([df, df2])
        query_output = df.to_html()
    return render_template("product_table.html", query_output=query_output)


if __name__ == "__main__":
    app.run(port, debug=True)


