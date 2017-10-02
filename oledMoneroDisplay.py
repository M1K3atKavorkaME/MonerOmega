import os
import json
import base64
import urllib3
http = urllib3.PoolManager()
from OmegaExpansion import oledExp

baseUrl     = "https://cnhv.co/28z0"

### MAIN PROGRAM ###
def print 'Got monero! ', monero
    # display the monero on the OLED
    oledWriteMonero(monero['text'], monero['date'])

    print 'Done!'

if __name__ == "__main__":
	mainProgram()
