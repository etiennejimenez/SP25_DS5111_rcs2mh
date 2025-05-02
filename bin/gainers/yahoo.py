"""
Downloads, processes, and timestamps Yahoo gainers before saving them
"""
import os
from datetime import datetime
import pandas as pd
from bin.gainers.base import GainerProcess#, GainerDownload
from bin.gainers.download import GainerDownload

# pylint: disable=too-few-public-methods
class GainerDownloadYahoo(GainerDownload):
    """
    Downloads Yahoo gainers in HTML format.
    """
    def __init__(self):
        """
        Method to initialize.
        """

    def download(self):
        """
        Method to download Yahoo gainers HTML
        """
        command ="""sudo google-chrome-stable \
                --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 \
                'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' \
                > ygainers.html"""
        os.system(command)
        convert_command = """python -c 'import pandas as pd; \
                          raw = pd.read_html("ygainers.html"); \
                          raw[0].to_csv("ygainers.csv")'"""
        os.system(convert_command)

class GainerProcessYahoo(GainerProcess):
    """
    Processes and saves with timestamp.
    """
    def __init__(self):
        """
        Method to initialize
        """

    def normalize(self):
        """
        Normalizes Yahoo gainers in a CSV file
        """
        df = pd.read_csv('ygainers.csv')
        csv_norm = pd.DataFrame()
        norm = df[['Symbol', 'Price', 'Change', 'Change %']]
        norm = norm.rename(columns = {'Symbol': 'symbol',
                                      'Price': 'price',
                                      'Change': 'price_change',
                                      'Change %': 'price_percent_change'})

        assert isinstance(norm['price'], pd.Series), f"expected pandas Series but got {type(norm['price'])}"
        assert isinstance(norm['price_change'][0], float), f"expected list of floats but first value is {type(norm['price_change'])}"
        assert len(norm['symbol']) > 1, "symbol list should not be empty!"

        #norm['price'] = norm['price'].str.extract(r'([^ ]+)')
        #norm['price'] = [x.replace(",", "") for x in norm['price'] if isinstance(x, str)]
        
        norm['price'] = norm['price'].astype(str).str.extract(r'([^ ]+)')[0].str.replace(',', '').astype(float)
        #norm['price'] = [float(x) for x in norm['price'] if isinstance(x, str)]

        norm['price_percent_change'] = norm['price_percent_change'].replace({r'\+': '', r'\%': ''}, regex=True)
        norm['price_percent_change'] = [float(x) for x in norm['price_percent_change']]

        csv_norm = norm.to_csv('ygainers_norm.csv')

    def save_with_timestamp(self):
        """
        Saves the Yahoo gainers CSV with a timestamp.
        """
        storage_path = '/home/ubuntu/SP25_DS5111_rcs2mh/collected_data/'
        current_time = datetime.fromtimestamp(datetime.now().timestamp())
        current_time = str(current_time)[:-7]
        print("Saving Yahoo gainers")
        filename = "ygainers" + current_time + ".csv"
        filename = filename.replace(' ','_')
        os.rename('ygainers.csv', storage_path + filename)
