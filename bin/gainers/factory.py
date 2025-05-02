"""
This module sends instructions to Gainers.
"""

from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ

class GainerFactory:
    """
    Class to call WSJ or Yahoo classes 
    """
    def __init__(self, choice):
        """
        Method to initialize
        """
        assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """
        Start the correct downloader
        """
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        if self.choice == 'wsj':
            return GainerDownloadWSJ()
        raise ValueError(f"Unrecognized gainer type: {self.choice}")

    def get_processor(self):
        """
        Start process to obtain csv for the correct gainer
        """
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        if self.choice == 'wsj':
            return GainerProcessWSJ()
        raise ValueError(f"Unrecognized gainer type: {self.choice}")
