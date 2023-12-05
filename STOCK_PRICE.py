import json
import urllib.request
import random
import time  


QUERY = "https://api.example.com/stock-quotes?token={}"  # Replace with your actual query string
N = 10  # Replace with your actual value for N

def getDatapoint(quote):
    """ Produce all of the needed values to generate a datapoint """
    """ ----------- update this function -----------"""
    stock = quote['stock']
    bid_price=float(quote['top_bid']['price'])
    ask_price=float(quote['top_ask']['price'])
    price=(bid_price + ask_price) / 2
    return stock,bid_price,ask_price,price

def getRatio(price_a,price_b):
    """ Get ratio of price_a and price_b """
    """ ----------- Update this function ----------- """
    """ Also create some unit tests for this function in client_test.py """
    if (price_b==0):
        # when price_b is 0 avoid throwing ZeroDivisionError
        ratio= None
    else  :
        ratio = price_a / price_b
    return  ratio
def main():
    
        # Query the price once every N seconds.
        prices={}
        for _ in iter(range(N)):
            
            quotes = [
                {'stock': 'ABC', 'top_bid': {'price': '100'}, 'top_ask': {'price': '102'}},
                {'stock': 'DEF', 'top_bid': {'price': '75'}, 'top_ask': {'price': '77.5'}}
            ]
            """ ----------- update to get the ratio ----------- """
          
            for quote in quotes:
                stock,bid_price,ask_price,price=getDatapoint(quote)
                prices[stock]=price
                print("Quoted %s at (bit:%s, ask:%s, price:%s)"%(stock,bid_price,ask_price,price))
                prices[stock]=price
                print("Ratio %s" %  getRatio(prices.get("ABC",0), prices.get("DEF",0)))
            time.sleep(1)
if __name__=="__main__":
    main()
        
        