"""
Module calls to the appropriate gainer script to download the gainers.
"""
from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods
class GainerDownload(ABC):#, url):
    """
    Downloads the HTML version of the respective gainer.
    """

    def __init__(self):
        """
        Initializer function
        """
        #self.url = url
        #pass

    @abstractmethod
    def download(self):
        """
        Creation of download function
        """
        #pass
