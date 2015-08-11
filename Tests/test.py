











{
 "kind": "qpxExpress#tripsSearch",
 "trips": {
  "kind": "qpxexpress#tripOptions",
  "requestId": "kuz5PUmNt1U75RJau0Mctj",
  "data": {
   "kind": "qpxexpress#data",
   "airport": [
    {
     "kind": "qpxexpress#airportData",
     "code": "JFK",
     "city": "NYC",
     "name": "New York John F Kennedy International"
    },
    {
     "kind": "qpxexpress#airportData",
     "code": "SFO",
     "city": "SFO",
     "name": "San Francisco International"
    }
   ],
   "city": [
    {
     "kind": "qpxexpress#cityData",
     "code": "NYC",
     "name": "New York"
    },
    {
     "kind": "qpxexpress#cityData",
     "code": "SFO",
     "name": "San Francisco"
    }
   ],
   "aircraft": [
    {
     "kind": "qpxexpress#aircraftData",
     "code": "32S",
     "name": "Airbus A320"
    }
   ],
   "tax": [
    {
     "kind": "qpxexpress#taxData",
     "id": "ZP",
     "name": "US Flight Segment Tax"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "AY_001",
     "name": "US September 11th Security Fee"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "US_001",
     "name": "US Transportation Tax"
    },
    {
     "kind": "qpxexpress#taxData",
     "id": "XF",
     "name": "US Passenger Facility Charge"
    }
   ],
   "carrier": [
    {
     "kind": "qpxexpress#carrierData",
     "code": "B6",
     "name": "Jetblue Airways Corporation"
    }
   ]
  },
  "tripOption": [
   {
    "kind": "qpxexpress#tripOption",
    "saleTotal": "USD259.10",
    "id": "N7RGinFv3PRUHNHHzaT6O8001",
    "slice": [
     {
      "kind": "qpxexpress#sliceInfo",
      "duration": 322,
      "segment": [
       {
        "kind": "qpxexpress#segmentInfo",
        "duration": 322,
        "flight": {
         "carrier": "B6",
         "number": "916"
        },
        "id": "G-zM+tqujpCMncSg",
        "cabin": "COACH",
        "bookingCode": "Z",
        "bookingCodeCount": 1,
        "marriedSegmentGroup": "0",
        "leg": [
         {
          "kind": "qpxexpress#legInfo",
          "id": "LvJQBgySnrzbFGvW",
          "aircraft": "32S",
          "arrivalTime": "2015-11-21T00:07-05:00",
          "departureTime": "2015-11-20T15:45-08:00",
          "origin": "SFO",
          "destination": "JFK",
          "originTerminal": "I",
          "destinationTerminal": "5",
          "duration": 322,
          "onTimePerformance": 90,
          "mileage": 2579,
          "meal": "Meal",
          "secure": true
         }
        ]
       }
      ]
     }
    ],
    "pricing": [
     {
      "kind": "qpxexpress#pricingInfo",
      "fare": [
       {
        "kind": "qpxexpress#fareInfo",
        "id": "AZQyn+p/+GZGIZb0MbX+Qlz0tO3RP741dxJ5xGVwy/7f1NUiZN+vsE7eDq3FFsbF+j8exM3FGhtQFvmZObeIiSylF5iPkO/ByKN/+YOIeUArd/AwuxmY9+huJlPsxHxVdRnl6PRM9wJSYd/",
        "carrier": "B6",
        "origin": "SFO",
        "destination": "NYC",
        "basisCode": "ZH4AUEN5",
        "private": true
       }
      ],
      "segmentPricing": [
       {
        "kind": "qpxexpress#segmentPricing",
        "fareId": "AZQyn+p/+GZGIZb0MbX+Qlz0tO3RP741dxJ5xGVwy/7f1NUiZN+vsE7eDq3FFsbF+j8exM3FGhtQFvmZObeIiSylF5iPkO/ByKN/+YOIeUArd/AwuxmY9+huJlPsxHxVdRnl6PRM9wJSYd/",
        "segmentId": "G-zM+tqujpCMncSg",
        "freeBaggageOption": [
         {
          "kind": "qpxexpress#freeBaggageAllowance",
          "bagDescriptor": [
           {
            "kind": "qpxexpress#bagDescriptor",
            "commercialName": "UPTO50LB 23KG AND62LI 158LCM",
            "count": 1,
            "description": [
             "Up to 50 lb/23 kg",
             "Up to 62 li/158 lcm"
            ],
            "subcode": "0GO"
           }
          ],
          "pieces": 0
         }
        ]
       }
      ],
      "baseFareTotal": "USD227.91",
      "saleFareTotal": "USD227.91",
      "saleTaxTotal": "USD31.19",
      "saleTotal": "USD259.10",
      "passengers": {
       "kind": "qpxexpress#passengerCounts",
       "adultCount": 1
      },
      "tax": [
       {
        "kind": "qpxexpress#taxInfo",
        "id": "US_001",
        "chargeType": "GOVERNMENT",
        "code": "US",
        "country": "US",
        "salePrice": "USD17.09"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "AY_001",
        "chargeType": "GOVERNMENT",
        "code": "AY",
        "country": "US",
        "salePrice": "USD5.60"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "XF",
        "chargeType": "GOVERNMENT",
        "code": "XF",
        "country": "US",
        "salePrice": "USD4.50"
       },
       {
        "kind": "qpxexpress#taxInfo",
        "id": "ZP",
        "chargeType": "GOVERNMENT",
        "code": "ZP",
        "country": "US",
        "salePrice": "USD4.00"
       }
      ],
      "fareCalculation": "SFO B6 NYC 227.91ZH4AUEN5 USD 227.91 END ZP SFO XT 17.09US 4.00ZP 5.60AY 4.50XF SFO4.50",
      "latestTicketingTime": "2015-08-06T23:59-04:00",
      "ptc": "ADT"
     }
    ]
   }
  ]
 }
}






# import urllib2
# import json

# url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCyyvZo3s217blnQ_fDVvnSKVILq98neFc"
# code = {
#     "request": {
#         "passengers": {
#             "kind": "qpxexpress#passengerCounts",
#             "adultCount": 1,
#         },
#         "slice": [
#             {
#                 "kind": "qpxexpress#sliceInput",
#                 "origin": "SFO",
#                 "destination": "NYC",
#                 "date": "2015-11-20",
#             }
#         ],
#         "refundable": "false",
#         "solutions": 5
#     }
# }
# jsonreq = json.dumps(code, encoding='utf-8')
# print jsonreq
# req = urllib2.Request(url, jsonreq, {'Content-Type': 'application/json'})
# flight = urllib2.urlopen(req)
# response = flight.read()
# flight.close()
# # print response
