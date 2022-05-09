import requests
import matplotlib as plt
import pandas as pd
from datetime import date
import csv

def get_stock_price(ticker_symbol, api):
	url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
	response = requests.get(url).json() # Getting information from the API
	price = response['price'][:-3]
	return price

def get_stock_quote(ticker_symbol, api):
	url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
	response = requests.get(url).json() # Getting information from the API
	return response

ticker = input("Enter the stock name (ex. NVDA): ")
with open("api.txt", "r") as f:
	api_key = f.readline() # Getting the API Key so it doesn't get exposed on the GitHub Repository
stockdata = get_stock_quote(ticker, api_key)
stock_price = get_stock_price(ticker, api_key)

# Getting Stock Data

exchange = stockdata['exchange']
name = stockdata['name']
open_price = stockdata['open']
high = stockdata['high']
low = stockdata['low']
volume = stockdata['volume']
percentage_change = stockdata['percent_change']
close_price = stockdata['close']
fiftytwo_week_high = stockdata['fifty_two_week']['high']
fiftytwo_week_low = stockdata['fifty_two_week']['low']
previous_close = stockdata['previous_close']
today = date.today()
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# Printing the information on the console
print(f"Exchange: {exchange}\nVolume: {volume}")
print("-------------------------------------------")
print(f"{name}: {stock_price}")
print("-------------------------------------------")
print(f"Open: {open_price}\nHigh: {high}\nLow: {low}\nClose: {close_price}\nPrevious Close: {previous_close}\nPercentage Change: {percentage_change}%")
print("-------------------------------------------")
print(f"52 Week High: {fiftytwo_week_high}\n52 Week Low: {fiftytwo_week_low}")

print("-------------------------------------------")
# Writing to CSV File
got_in = False
file_name = ticker + ".csv"
print(f"File is {file_name}")
with open(file_name, "r") as file:
	to_read = csv.reader(file)
	for row in to_read:
		got_in = True
		print(row)

if got_in == False:
	with open(file_name, "a") as file_empty:
		empty_writer = csv.writer(file_empty)
		header = ['Name', 'Date', 'Stock Price', 'Open', 'Close', 'Percentage Change', 'Fifty Two Week High', 'Fifty Two Week Low']
		empty_writer.writerow(header)

else:
	with open(file_name, "a") as file_full:
		full_writer = csv.writer(file_full)
		header = [ticker,d2,stock_price, open_price, close_price, percentage_change, fiftytwo_week_high, fiftytwo_week_low]
		full_writer.writerow(header)

df = pd.read_csv('NVDA.csv')

table = input("Would you like to see the table? (y/n): ")
if table == "y":
	print(df.to_string()) 

else:
	print("Okay, bye!")