import os
import json
import base64
import urllib3
http = urllib3.PoolManager()
from OmegaExpansion import oledExp

baseUrl     = "https://cnhv.co/28z0"

    # perform the request
    r = http.request(
        url
    )

    # convert the response data to a dictionary
    responseData = json.loads(r.data.decode('utf-8'))


# function to read the last monero from a user's timeline
def Monero(userId):
    url = baseUrl
    params = {
    }

    # create the request headers
    headers = {
    }

    # execute the GET request
    r = http.request(
        'GET',
        url
    )


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
