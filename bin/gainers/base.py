"""
Base class to process commands
"""

class GainerProcess:
    """
    Class to process commands
    """
    def __init__(self, gainer_downloader, gainer_normalizer):
        """
        Method for initialization
        """
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        """
        Calls the correct download method
        """
        self.downloader.download()

    def _normalize(self):
        """
        Calls the correct normalize method
        """
        self.normalizer.normalize()

    def _save_to_file(self):
        """
        Saves with timestamp method
        """
        self.normalizer.save_with_timestamp()

    def process(self):
        """
        Runs each call
        """
        self._download()
        self._normalize()
        self._save_to_file()
