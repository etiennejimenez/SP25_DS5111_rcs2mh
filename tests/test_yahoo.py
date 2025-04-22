"""
Test for yahoo.py
"""
import pandas as pd
import sys
import os
sys.path.append('.')
from bin.gainers.factory import GainerFactory

def test_download():
    """
    Tests correct download of HTML and creation of CSV
    """

    gf = GainerFactory('yahoo')
    gf.get_downloader()
    assert os.path.exists('ygainers.html')

def test_normalize_csv():
    """
    Tests correct normalization for yahoo.py
    """

    df = pd.read_csv('ygainers_norm.csv')
    #assert set(df.columns) == {'symbol', 'price', 'price_change', 'price_percent_change'}
    
    assert df['symbol'].dtype == 'object'
    assert df['price'].dtype == 'float64'
    assert df['price_change'].dtype == 'float64'
    assert df['price_percent_change'].dtype == 'float64'

def test_save_with_timestamp():
    """
    Tests file is saved with the correct timestamp
    """

    assert os.listdir('collected_data/')

