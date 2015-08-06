import urllib2
import json

api_url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCyyvZo3s217blnQ_fDVvnSKVILq98neFc"
flight_request = {
    "request": {
        "passengers": {
            "kind": "qpxexpress#passengerCounts",
            "adultCount": 1,
        },
        "slice": [
            {
                "kind": "qpxexpress#sliceInput",
                "origin": "SFO",
                "destination": "PDX",
                "date": "2015-11-20",
            }
        ],
        "refundable": "false",
        "solutions": 1
    }
}
jsonreq = json.dumps(flight_request, encoding='utf-8', indent=1)
req = urllib2.Request(api_url, jsonreq, {'Content-Type': 'application/json'})
flight = urllib2.urlopen(req)
response = flight.read()
flight.close()
print jsonreq