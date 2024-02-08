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

        cursor.execute("SELECT TOP (10) * FROM [SalesLT].[Address] ORDER BY [AddressID] DESC")
        row = cursor.fetchall()
    return render_template("product_table.html", query_output=row)


@app.route("/edit", methods=['POST', 'PUT',  'GET', 'DELETE'])
def edit():
    """Performs query to DB but display using template"""
    if request.method == 'GET':
        with conn.cursor() as cursor:
            cursor.execute(f"""SELECT [AddressID],
                                [AddressLine1],
                                [City],
                                [StateProvince],
                                [CountryRegion],
                                [PostalCode]
                            FROM [SalesLT].[Address]
                            WHERE [AddressID]=''""")
            return render_template("index.html")
    elif request.method == 'POST':
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE [SalesLT].[Address]
                SET [AddressLine1] = ?,
                    [AddressLine2] = ?,
                    [City] = ?,
                    [StateProvince] = ?,
                    [CountryRegion] = ?,
                    [PostalCode] = ?,
                    [rowguid] = ?,
                    [ModifiedDate] = ?
                WHERE [AddressID] = ?""", (
                    request.form['AddressLine1'],
                    request.form['AddressLine2'],
                    request.form['City'],
                    request.form['StateProvince'],
                    request.form['CountryRegion'],
                    request.form['PostalCode'],
                    request.form['rowguid'],
                    request.form['ModifiedDate'],
                    request.form['id']  # Assuming you have this in your form
                ))
            conn.commit()
        return redirect("/product_table")

    elif request.method == 'PUT':
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO [SalesLT].[Address](
                AddressLine1,
                AddressLine2,
                City,
                StateProvince,
                CountryRegion,
                PostalCode,
                ModifiedDate
                )
                VALUES (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
                )""", (
                request.form['AddressLine1'],
                request.form['AddressLine2'],
                request.form['City'],
                request.form['StateProvince'],
                request.form['CountryRegion'],
                request.form['PostalCode'],
                request.form['ModifiedDate']
            ))
            conn.commit()
        return redirect("/product_table")
    elif request.method == 'DELETE':
        with conn.cursor() as cursor:
            cursor.execute("""DELETE FROM [SalesLT].[Address] WHERE [AddressID] = ?""",
                           (request.form['id']))
            conn.commit()
        return redirect("/product_table")
    else:
        pass


if __name__ == "__main__":
    app.run(port, debug=True)


