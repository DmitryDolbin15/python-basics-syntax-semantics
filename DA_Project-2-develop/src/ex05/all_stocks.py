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
        
def stock_prices(slova):
    for s in slova :
        if s.capitalize() in COMPANIES:
            val_comp = COMPANIES[s.capitalize()]
            val_ston = STOCKS.get(val_comp, "Unknown price")
            print(f"{s.capitalize()} stock price is {val_ston}")
        elif s.upper() in STOCKS:
            comp_n = get_key(COMPANIES, s.upper())
            if comp_n :
                print(f"{s.upper()} is a ticker symbol for {comp_n}")
            else:
                print(f"{s} is an unknown company or an unknown ticker symbol")

        else:
            print(f"{s} is an unknown company or an unknown ticker symbol")


if __name__ == "__main__":
    if len(sys.argv) == 2 :
        t = sys.argv[1].split(',')
        l = len(t)
        if l == 3 :
            slova = [sl.strip() for sl in t]
            if (all(s !=  '' for s in slova) ):
                stock_prices(slova)