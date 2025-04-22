"""
Test for wsj.py
"""
import pandas as pd
import os
import sys
sys.path.append('.')
from bin.gainers.factory import GainerFactory


def test_download():
    """
    Tests correct download of HTML and creation of CSV
    """

    gf = GainerFactory('wsj')
    gf.get_downloader()
    assert os.path.exists('wsjgainers.html')
    
def test_normalize_csv():
    """
    Tests correct normalization for wsj.py
    """

    df = pd.read_csv('wsjgainers_norm.csv')
    #assert set(df.columns) == {'symbol', 'price', 'price_change', 'price_percent_change'}
    
    assert df['symbol'].dtype == 'object'
    assert df['price'].dtype == 'float64'
    assert df['price_change'].dtype == 'float64'
    assert df['price_percent_change'].dtype == 'float64'

def test_save_with_timestamp():
    """
    Test function to for timestamp in filename.
    """

    assert os.listdir('collected_data/')
