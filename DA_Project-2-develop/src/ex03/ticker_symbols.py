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

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
def stock_prices():
    comp = sys.argv[1].upper()
    key_from_stock = STOCKS.get(comp, "Unknown company")
    if key_from_stock != "Unknown company":
        key_from_comp = get_key(COMPANIES, comp)
        print(key_from_comp,key_from_stock)
    else:
        print(key_from_comp)

if __name__ == "__main__":
    if len(sys.argv) == 2 :
        stock_prices()