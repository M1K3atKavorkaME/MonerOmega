import os
import json
import base64
import urllib3
http = urllib3.PoolManager()
from OmegaExpansion import oledExp

baseUrl     = "https://cnhv.co/28z0"

def oledWriteMonero(text, date):
    if oledExp.driverInit() != 0:
        print 'ERROR: Could not initialize the OLED Expansion'
        return False

    # set the cursor to the next line
    oledExp.setCursor(1,0)

    # write out the monero
    oledExp.write(text)



### MAIN PROGRAM ###
def mainProgram():
    # find the directory of the script
    dirName = os.path.dirname(os.path.abspath(__file__))

    print 'Got monero! ', monero
    # display the monero on the OLED
    oledWriteMonero(monero['text'], monero['date'])

    print 'Done!'


if __name__ == "__main__":
	mainProgram()
