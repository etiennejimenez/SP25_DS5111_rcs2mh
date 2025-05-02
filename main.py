"""
Performs the main action by calling all the other modules.
"""

import sys
import bin.gainers.factory as gf
import bin.gainers.base as base
print(sys.argv[0])
print(sys.argv[1])
choice = sys.argv[1]

# Factory calls the appropriate methods to get CSVs
factory = gf.GainerFactory(choice)
downloader = factory.get_downloader()
normalizer = factory.get_processor()

# Processes each respective gainer
processor = base.GainerProcess(downloader, normalizer)
processor.process()
