# NOTE: This file was changed according to Part 2, Step 8x. 
# Enter the following commands to import the modules and disable SSL
# certificate warnings:
import json
import requests
requests.packages.urllib3.disable_warnings()

# Create a string variable to hold the API endpoint URI and two dictionaries,
# one for the request header and one for the body JSON.
api_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces/interface=Loopback99"

# Create a dictionary variable named headers that has keys for Accept
# and Content-type and assign the keys the value "application/yang-data+json"
headers = {"Accept": "application/yang-data+json",
           "Content-type":"application/yang-data+json"
           }

# Create a Python tuple variable named basicauth that has two keys needed
# for authentication, username and password.
basicauth = ("admin", "C1sco12345")

# The variables created in the previous step will be used as parameters
# for the requests.put() method. This method sends an HTTP PUT request to the
# RESTCONF API. You will assign the result of the request to a variable name
# resp. That variable will hold the JSON response from the API.
resp = requests.delete(api_url, auth=basicauth, headers=headers, verify=False)
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print("Error code {}, reply: {}".format(resp.status_code, resp.json()))
