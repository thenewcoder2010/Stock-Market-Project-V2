import requests
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

# Printing the information on the console
print(f"Exchange: {exchange}\nVolume: {volume}")
print("-------------------------------------------")
print(f"{name}: {stock_price}")
print("-------------------------------------------")
print(f"Open: {open_price}\nHigh: {high}\nLow: {low}\nClose: {close_price}\nPrevious Close: {previous_close}\nPercentage Change: {percentage_change}%")
print("-------------------------------------------")
print(f"52 Week High: {fiftytwo_week_high}\n52 Week Low: {fiftytwo_week_low}")
print("-------------------------------------------")
#
file_name = ticker + ".csv"
with open(file_name, "a+") as file:
	reader = csv.reader(file)

