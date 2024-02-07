"""
This app shows how to perform CRUD (Create, Retrieve, Update, Delete) 
operations in Flask web application connected to MS SQL Server.
"""

import os
import pyodbc
from flask import Flask,render_template,request,url_for,redirect
from dotenv import load_dotenv


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


if __name__ == "__main__":
    app.run(port)