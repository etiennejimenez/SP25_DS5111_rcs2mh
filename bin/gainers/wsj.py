"""
Downloads, processes, and timestamps WSJ gainers before saving them.
"""
import os
from datetime import datetime
import pandas as pd
from bin.gainers.base import GainerProcess
from bin.gainers.download import GainerDownload

# pylint: disable=too-few-public-methods
class GainerDownloadWSJ(GainerDownload):
    """
    Downloads WSJ gainers in HTML format
    """
    def __init__(self):
        """
        Method to initialize
        """

    def download(self):
        """
        Method to download WSJ gainers HTML
        """
        command = """sudo google-chrome-stable \
                  --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 \
                  'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html"""
        os.system(command)
        convert_command = """python -c 'import pandas as pd; \
                           raw = pd.read_html("wsjgainers.html"); \
                           raw[0].to_csv("wsjgainers.csv")'"""
        os.system(convert_command)

class GainerProcessWSJ(GainerProcess):
    """
    Normalizes and saves WSJ gainers in CSV with a timestamp
    """

    def __init__(self):
        """
        Method to initialize
        """

    def normalize(self):
        """
        Normalizes WSJ gainers in a CSV file
        """
        df = pd.read_csv('wsjgainers.csv')
        csv_norm = pd.DataFrame()
        wsj = df[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
        wsj = wsj.rename(columns = {'Unnamed: 0': 'symbol',
                                    'Last': 'price',
                                    'Chg': 'price_change',
                                    '% Chg': 'price_percent_change'})

        assert isinstance(wsj['price'], pd.Series), f"expected pandas Series but got {type(wsj['price'])}"
        assert isinstance(wsj['price_change'][0], float), f"expected list of floats but first value is {type(wsj['price_change'])}"
        assert len(wsj['symbol']) > 1, "symbol list should not be empty!"

        wsj['symbol'] = wsj['symbol'].str.extract(r"\(([^)]+)\)")

        csv_norm = wsj.to_csv('wsjgainers_norm.csv')

    def save_with_timestamp(self):
        """
        Saves the WSJ gainers CSV with a timestamp.
        """
        storage_path = '/home/ubuntu/SP25_DS5111_rcs2mh/collected_data/'
        current_time = datetime.fromtimestamp(datetime.now().timestamp())
        current_time = str(current_time)[:-7]
        print("Saving WSJ gainers")
        filename = "wsjgainers" + current_time + ".csv"
        filename = filename.replace(' ','_')
        os.rename('wsjgainers.csv', storage_path + filename)
