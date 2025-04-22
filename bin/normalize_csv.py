import numpy as np
import pandas as pd

def normalizer(csv):
    
    if (csv == "ygainers.csv"):
        df = pd.read_csv(csv)
        norm = df[['Symbol', 'Price', 'Change', 'Change %']]
        norm = norm.rename(columns = {'Symbol': 'symbol', 
                                      'Price': 'price', 
                                      'Change': 'price_change', 
                                      'Change %': 'price_percent_change'})
        
        assert isinstance(norm['price'], pd.Series), f"expected pandas Series but got {type(norm['price'])}"
        assert isinstance(norm['price_change'][0], float), f"expected list of floats but first value is {type(norm['price_change'])}" 
        assert len(norm['symbol']) > 1, "symbol list should not be empty!"
        
        norm['price'] = norm['price'].str.extract(r'([^ ]+)')
        norm['price'] = [x.replace(",", "") for x in norm['price']]
        norm['price'] = [float(x) for x in norm['price']] 

        norm['price_percent_change'] = norm['price_percent_change'].replace({r'\+': '', r'\%': ''}, regex=True)
        norm['price_percent_change'] = [float(x) for x in norm['price_percent_change']] 

        csv_norm = norm.to_csv(f"{csv}_norm.csv")
    
    elif (csv == "wsjgainers.csv"):
        df = pd.read_csv('wsjgainers.csv')
        wsj = df[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
        wsj = wsj.rename(columns = {'Unnamed: 0': 'symbol',
                                    'Last': 'price', 
                                    'Chg': 'price_change', 
                                    '% Chg': 'price_percent_change'})

        assert isinstance(wsj['price'], pd.Series), f"expected pandas Series but got {type(norm['price'])}"
        assert isinstance(wsj['price_change'][0], float), f"expected list of floats but first value is {type(norm['price_change'])}"
        assert len(wsj['symbol']) > 1, "symbol list should not be empty!"
        
        wsj['symbol'] = wsj['symbol'].str.extract(r"\(([^)]+)\)")
        
        csv_norm = wsj.to_csv(f"{csv}_norm.csv")

    else:
        print("Try again!")
    
    return csv_norm
