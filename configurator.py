# PMP450 configuration generator

import csv
import sys
import json

# Declare files, load JSON data.
csvfile = open(sys.argv[1], 'r')
with open(sys.argv[2], 'r') as template:
    templateJson = json.load(template)


# Declare CSV Fieldnames to scan
fieldNames = ("Name","macAddress", "ipAddress", "subnetMask", "gatewayAddress", "Zone")
# Create a dictionary of CSV values.
reader = csv.DictReader( csvfile, fieldNames)
# Skip the header (first) row
next(reader)
# Iterate over values and write to JSON.
for row in reader:
    # Logic for determing color code primary or secondary
    if row["Zone"] == "1":
        templateJson["userParameters"]["smRadioConfig"]["colorCodeList"][0]["colorCode"] = 254
        templateJson["userParameters"]["smRadioConfig"]["colorCodeList"][0]["priority"] = 1
        templateJson["userParameters"]["smRadioConfig"]["colorCodeList"][1]["colorCode"] = 128
        templateJson["userParameters"]["smRadioConfig"]["colorCodeList"][1]["priority"] = 2

    elif row["Zone"] == "2":
        templateJson["userParameters"]["smRadioConfig"]["colorCodeList"][0]["colorCode"] = 128
        templateJson["userParameters"]["smRadioConfig"]["colorCodeList"][0]["priority"] = 1
        templateJson["userParameters"]["smRadioConfig"]["colorCodeList"][1]["colorCode"] = 254
        templateJson["userParameters"]["smRadioConfig"]["colorCodeList"][1]["priority"] = 2

    # Set the rest of the parameters
    templateJson["userParameters"]["location"]["siteName"] = row["Name"]
    templateJson["userParameters"]["networkConfig"]["lanIp"] = row["ipAddress"]
    templateJson["userParameters"]["networkConfig"]["lanMask"] = row["subnetMask"]
    templateJson["userParameters"]["networkConfig"]["lanGateway"] = row["gatewayAddress"]
    with open("configs/" + row["macAddress"].lower() + ".cfg", 'wt') as cfgFile:
        json.dump(templateJson, cfgFile, sort_keys=True, indent=1)
