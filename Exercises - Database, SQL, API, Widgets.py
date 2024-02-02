# Exercises - Database, SQL, API, Widgets

#Exercice 1

import sqlite3
# create a connection object
conn = sqlite3.connect("new_nb_2024.db")

#create a cursor to run SQL queries
cursor = conn.cursor()

#Execute SQL query create a new Table "Students"
cursor.execute('''CREATE TABLE if not exists Students(ID INT PRIMARY KEY, NAME TEXT, CITY NAME)''')

#Ask the user to input information
user_id = input("Please input a User ID :")
user_name = input("Please enter a name :")
user_city = input("Please enter a city :")

#Push this information in the database
cursor.execute('''INSERT INTO Students(ID, NAME, CITY) VALUES(?, ?, ?)''', (user_id, user_name, user_city))

#Commit to the database and close
conn.commit()
conn.close()


#Exercice 2

def count_database_items(db, table):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM'+ table)
    x = cursor.fetchall()
    return len(x)

count_database_items("new_nb_2024.db", "Students")


#Exercice 3

import yfinance as yf
import pandas as pd, numpy as np
from ipywidgets import widgets

start_date = "2013-01-01"
end_date = "2023-12-31"
list_underlyings = ["AAPL", "MSFT", "EURUSD = X"]
list_var_percentile = [0.1, 0.1, 1, 10, 50, 90]

#widgets
button = widgets.button(Description = "Compute VaR")
widget_underlying_list = widgets.dropdown(options = list_underlyings, value = "MSFT")
widget_percentile_list = widgets.dropdown(options = list_var_percentile, value = 0.1)
widget_ouput = widgets.output()
display(widget_underlying_list, widget_percentile_list, button, widget_ouput)

def compute_var(_): #function to compute the VaR
  underlying = widget_underlying_list.value #selected underlying
  percentile = widget_percentile_list.value #selected percentile
  ticker = yf.Tickers(underlying) #loading the yahoo ticker
  df_yahoo_data = ticker.tickers[underlying].history(start = start_date, end = end_date)
  df_returns = df_yahoo_data[("Close")].pct_change().dropna()
  VaR = np.percentile(df_returns, percentile)*100
  #with widget _ouptput
  print(f"The VaR of {underlying} at {percentile}% confidence level is {VaR}%")
  
#link between the button and the function
button.on_click(compute_var)