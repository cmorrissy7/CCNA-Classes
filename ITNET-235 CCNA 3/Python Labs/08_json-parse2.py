# request module includes functions for retrieving JSON data from a URL.
# urllib.parse includes functions for parsing and manipulating the JSON data.

import urllib.parse
import requests

# main_api is the main url to access
# key is the MapQuest API retrieved from MapQuest

main_api = "http://www.mapquestapi.com/directions/v2/route?"
key = "zwICPUktgV0UwlxIqjg59DkBMwxftVRY"

# Create a while loop which allows the use to continue making requests.
# The orig and dest variables will take user input for locations.
# url variable will combine other variables to create the URL.
# The .urlencode method is used to properly format the address value.

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    # Print the constructed URL so the user can see.
    print("URL: " + (url))

    # create json_data variable that makes use of the get method of the
    # requests module and specifies JSON as the requested format.
    json_data = requests.get(url).json()

    # Parse the JSON data to obtain the statuscode value.
    json_status = json_data["info"]["statuscode"]

    # If the request is successful, print the information.
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        # for loop iterates through each maneuvers list and prints the narrative, converts
        # miles to kilometers, and formats the kilometer value.
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")

    # else, if the status code is 402, print it and a message about invalid location.
    elif json_status == 402:
        print("\n****************************************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("****************************************************************\n")

    # else, if status code is something other than 0 or 402, print the status code and
    # a link to mapquest's status code information.
    else:
        print("\n************************************************************************")
        print("Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
