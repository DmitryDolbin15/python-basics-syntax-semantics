import sys

COMPANIES = {
  'Apple': 'AAPL',
  'Microsoft': 'MSFT',
  'Netflix': 'NFLX',
  'Tesla': 'TSLA',
  'Nokia': 'NOK'
  }

STOCKS = {
  'AAPL': 287.73,
  'MSFT': 173.79,
  'NFLX': 416.90,
  'TSLA': 724.88,
  'NOK': 3.37
  }

def stock_prices():
    comp = sys.argv[1].capitalize()
    key_from_comp = COMPANIES.get(comp, "Unknown company")
    
    if key_from_comp != "Unknown company":
        key_from_stock= STOCKS.get(key_from_comp, "Unknown company")
        print(key_from_stock)
    else:
        print(key_from_comp)

if __name__ == "__main__":
    if len(sys.argv) == 2 :
        stock_prices()