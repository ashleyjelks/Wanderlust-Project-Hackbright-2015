import urllib2
import json

url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCyyvZo3s217blnQ_fDVvnSKVILq98neFc"
code = {
    "request": {
        "passengers": {
            "kind": "qpxexpress#passengerCounts",
            "adultCount": 1,
        },
        "slice": [
            {
                "kind": "qpxexpress#sliceInput",
                "origin": "SFO",
                "destination": "NYC",
                "date": "2015-11-20",
            }
        ],
        "refundable": "false",
        "solutions": 5
    }
}
jsonreq = json.dumps(code, encoding='utf-8')
print jsonreq
req = urllib2.Request(url, jsonreq, {'Content-Type': 'application/json'})
flight = urllib2.urlopen(req)
response = flight.read()
flight.close()
# print response
