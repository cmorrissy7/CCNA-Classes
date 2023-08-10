# Enter the following commands to import the modules and disable SSL
# certificate warnings:
import json
import requests
requests.packages.urllib3.disable_warnings()

# Create a string variable to hold the API endpoint URI and two dictionaries,
# one for the request header and one for the body JSON.
api_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces"

# Create a dictionary variable named headers that has keys for Accept
# and Content-type and assign the keys the value "application/yang-data+json"
headers = {"Accept": "application/yang-data+json",
           "Content-type":"application/yang-data+json"
           }

# Create a Python tuple variable named basicauth that has two keys needed
# for authentication, username and password.
basicauth = ("admin", "C1sco12345")

# The variables created in the previous step will be used as parameters
# for the requests.get() method.
# Assign the result of the request to a variable named "resp". That variable
# will hold the JSON response from the API. If the request is successful,
# the JSON will contain the returned YANG data model.
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

# The response JSON is not compatible with Python dictionary and list objects
# so it is converted to Python format. Create a new variable called
# response_json and assign the variable resp to it, adding the json()
# method to convert the JSON.
response_json = resp.json()

# You can verify that your code returns the JSON in the IDLE Shell
# by temporarily adding a print statement to your script.
# To prettify the output, use the json.dumps() function
# with the “indent” parameter:
print(json.dumps(response_json, indent=4))
