import urllib2
import json
import pprint
# from time import sleep

#PrettyPrint takes a dictionary and turns it into human readable  organization
api_url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCyyvZo3s217blnQ_fDVvnSKVILq98neFc"


def get_price(origin, destination, departure_date, return_date, max_price=1500):

    flight_request = {
        "request": {
            "passengers": {
                "kind": "qpxexpress#passengerCounts",
                "adultCount": 1,
            },
            "slice": [
                {
                    "kind": "qpxexpress#sliceInput",
                    "origin": origin,
                    "destination":  destination,
                    "date": departure_date,
                    "maxStops": 1,
                    "maxPrice": max_price
                },
                {
                    "kind": "qpxexpress#sliceInput",
                    "origin": destination,
                    "destination": origin,
                    "date": return_date,
                    "maxStops": 1,
                    "maxPrice": max_price
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
    parsed_json = json.loads(response)

    printer = pprint.PrettyPrinter()
    printer.pprint(parsed_json)
    return parsed_json

#len(s['trips']['tripOption'][0]['slice'])

# def seed_response(response):

#     flight_id = pass
#     origin_city_name = response['trips']['data']['city'][1]['name']
#     origin_airport_name = response['trips']['data']['airport'][1]['name']
#     origin_airport_code = response['trips']['data']['city'][1]['code']
#     destination_city_name =  response['trips']['data']['city'][0]['name']
#     destination_airport_name = response['trips']['data']['airport'][0]['name']
#     destination_airport_code = response['trips']['data']['city'][0]['code']
#     date_time_departing_flight_arrives = 
#     date_time_departing_flight_departs = 
#     date_time_return_flight_arrives = 
#     date_time_return_flight_departs = 
#     airline = 
#     flight_number = 
#     base_fare = 
#     taxes = 
#     total_fare = 
#     destination_region = 
#     first_connection_city_name = response['trips']['data']['city'][2]['name']
#     first_connection_airport_name = response['trips']['data']['airport'][2]['name']
#     first_connection_airport_code = response['trips']['data']['city'][2]['code']
#     first_connection_date_time_departs = 
#     first_connection_date_time_arrives =

