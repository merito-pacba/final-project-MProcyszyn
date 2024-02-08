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


@app.route("/address_table")
def address_table():

    with conn.cursor() as cursor:

        cursor.execute("SELECT TOP (10) * FROM [SalesLT].[Address] ORDER BY [AddressID] DESC")
        row = cursor.fetchall()
    return render_template("address_table.html", query_output=row)


@app.route("/edit", methods=['POST', 'PUT',  'GET', 'DELETE'])
def edit():
    if request.method == 'POST':
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
        return redirect("/address_table")

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
        return redirect("/address_table")
    elif request.method == 'DELETE':
        with conn.cursor() as cursor:
            cursor.execute("""DELETE FROM [SalesLT].[Address] WHERE [AddressID] = ?""",
                           (request.form['id']))
            conn.commit()
        return redirect("/address_table")
    else:
        pass


@app.route("/product_table")
def product_table():

    with conn.cursor() as cursor:

        cursor.execute("SELECT TOP (10) * FROM [SalesLT].[Product] ORDER BY [ProductID] DESC")
        row = cursor.fetchall()
    return render_template("product_table.html", query_output=row)


@app.route("/edit_product", methods=['POST', 'PUT',  'GET', 'DELETE'])
def edit_product():
    """Performs query to DB but display using template"""
    if request.method == 'POST':
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE [SalesLT].[Product]
                SET [Name] = ?
                    ,[ProductNumber] = ?
                    ,[Color] = ?
                    ,[StandardCost] = ?
                    ,[ListPrice] = ?
                    ,[Size] = ?
                    ,[Weight] = ?
                    ,[ProductCategoryID] = ?
                    ,[ProductModelID] = ?
                    ,[SellStartDate] = ?
                    ,[SellEndDate] = ?
                    ,[DiscontinuedDate] = ?
                    ,[rowguid] = ?
                    ,[ModifiedDate] = ?
                    WHERE [ProductID] = ?""", (
                    request.form['Name'],
                    request.form['ProductNumber'],
                    request.form['Color'],
                    request.form['StandardCost'],
                    request.form['ListPrice'],
                    request.form['Size'],
                    request.form['Weight'],
                    request.form['ProductCategoryID'],
                    request.form['ProductModelID'],
                    request.form['SellStartDate'],
                    request.form['SellEndDate'],
                    request.form['DiscontinuedDate'],
                    request.form['rowguid'],
                    request.form['ModifiedDate'],
                    request.form['ProductID']
                ))
            conn.commit()
        return redirect("/product_table")

    elif request.method == 'PUT':
        with conn.cursor() as cursor:
            cursor.execute("""
                        INSERT INTO [SalesLT].[Product]
                        ( 
                            Name
                            ,ProductNumber
                            ,Color
                            ,StandardCost
                            ,ListPrice
                            ,Size
                            ,Weight
                            ,ProductCategoryID
                            ,ProductModelID
                            ,SellStartDate
                            ,SellEndDate
                            ,DiscontinuedDate
                            ,rowguid
                            ,ModifiedDate
                            VALUES(
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    ?,
                                    )"""), (
                            request.form['Name'],
                            request.form['ProductNumber'],
                            request.form['Color'],
                            request.form['StandardCost'],
                            request.form['ListPrice'],
                            request.form['Size'],
                            request.form['Weight'],
                            request.form['ProductCategoryID'],
                            request.form['ProductModelID'],
                            request.form['SellStartDate'],
                            request.form['SellEndDate'],
                            request.form['DiscontinuedDate'],
                            request.form['rowguid'],
                            request.form['ModifiedDate'],
                            request.form['ProductID']
            )
            conn.commit()
        return redirect("/product_table")
    elif request.method == 'DELETE':
        with conn.cursor() as cursor:
            cursor.execute("""DELETE FROM [SalesLT].[Product] WHERE [ProductID] = ?""",
                           (request.form['id']))
            conn.commit()
        return redirect("/product_table")
    else:
        pass


if __name__ == "__main__":
    app.run(port, debug=True)


