"""
Performs the main action by calling all the other modules.
"""

import sys
import bin.gainers.factory as gf
import bin.gainers.process as pr
choice = sys.argv[1]

# Factory calls the appropriate methods to get CSVs
factory = gf.GainerFactory(choice)
downloader = factory.get_downloader()
normalizer = factory.get_processor()

# Processes each respective gainer 
processor = pr.GainerProcess(downloader, normalizer)
processor.process()
