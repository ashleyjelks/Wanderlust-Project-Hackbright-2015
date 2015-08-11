import urllib2
import json
import pprint
from model import FlightLeg, Flight
from model import db
# from time import sleep

#PrettyPrint takes a dictionary and turns it into human readable  organization
api_url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCyyvZo3s217blnQ_fDVvnSKVILq98neFc"

USA_AIRPORT_CODES = ["SFO", "LAX", "PHX", "SEA", "DEN", "DFW", "IAH", "ORD",
                     "ATL", "MIA", "IAD", "PHL", "JFK", "BOS", "CLT", "LAS"]
CANADIAN_AIRPORT_CODES = ["YUL", "YYZ", "YVR", "HNL"]
MEXICO_CARIBBEAN_AIRPORT_CODES = ["NAS", "MBJ", "HAV", "BGI", "POS", "SJU", "GCM", "MEX", "CUN"]
LATIN_AMERICAN_AIRPORT_CODES = ["SJO", "PTY", "CTG", "BOG", "UIO", "LIM", "EZE", "GIG", "CCS", "GRU"]
EUROPEAN_AIRPORT_CODES = ["LIS", "MAD", "CDG", "LHR", "DUB", "FCO", "ZRH", "GVA", "MXP",
                          "AMS", "TXL", "BRU", "FRA", "ATH", "BUD", "WAW", "DME", "ARN", "CPH"]
AFRICAN_AIRPORT_CODES = ["CAI", "TUN", "RAK", "CMN", "DKR", "LOS", "JNB", "CPT", "DAR", "NBO"]
ASIAN_AIRPORT_CODES = ["BOM", "DEL", "CGK", "SIN", "KUL", "HKT", "BKK", "PEK", "HND", "HKG",
                       "PVG", "ICN", "SGN", "MNL"]
MIDDLE_EASTERN_AIRPORT_CODES = ["RUH", "DXB", "IST", "TLV"]
OCEANIAN_AIRPORT_CODES = ["SYD", "MEL", "AKL", "PPT", "POM"]
CITY_COMBOS = [("SFO", "LAX"),("SFO", "PHX"),("SFO", "SEA"),("SFO", "DEN"),("SFO", "DFW"),("SFO", "IAH"),("SFO", "ORD"),("SFO", "ATL"),("SFO", "MIA")] 
               # ("SFO", "IAD"),("SFO", "PHL"),("SFO", "JFK"),("SFO", "BOS"),("SFO", "CLT"),("SFO", "LAS"),("SFO", "YUL"),("SFO", "YYZ"),("SFO", "YVR")
               # ("SFO", "HNL"),("SFO", "NAS"),("SFO", "MBJ"),("SFO", "HAV"),("SFO", "BGI"),("SFO", "POS"),("SFO", "SJU"),("SFO", "GCM"),("SFO", "MEX")
               # ("SFO", "CUN"),("SFO", "SJO"),("SFO", "PTY"),("SFO", "CTG"),("SFO", "BOG"),("SFO", "UIO"),("SFO", "LIM"),("SFO", "EZE"),("SFO", "GIG")
               # ("SFO", "CCS"),("SFO", "GRU"),("SFO", "LIS"),("SFO", "MAD"),("SFO", "CDG"),("SFO", "LHR"),("SFO", "DUB"),("SFO", "FCO"),("SFO", "ZRH")
               # ("SFO", "GVA"),("SFO", "MXP"),("SFO", "AMS"),("SFO", "TXL"),("SFO", "BRU"),("SFO", "FRA"),("SFO", "ATH"),("SFO", "BUD"),("SFO", "WAW")
               # ("SFO", "DME"),("SFO", "ARN"),("SFO", "CPH"),("SFO", "CAI"),("SFO", "TUN"),("SFO", "RAK"),("SFO", "CMN"),("SFO", "DKR"),("SFO", "LOS")
               # ("SFO", "JNB"),("SFO", "CPT"),("SFO", "DAR"),("SFO", "NBO"),("SFO", "BOM"),("SFO", "DEL"),("SFO", "CGK"),("SFO", "SIN"),("SFO", "KUL")
               # ("SFO", "HKT"),("SFO", "BKK"),("SFO", "PEK"),("SFO", "HND"),("SFO", "HKG"),("SFO", "PVG"),("SFO", "ICN"),("SFO", "SGN"),("SFO", "MNL")
               # ("SFO", "RUH"),("SFO", "DXB"),("SFO", "IST"),("SFO", "TLV"),("SFO", "SYD"),("SFO", "MEL"),("SFO", "AKL"),("SFO", "PPT"),("SFO", "POM")]

def populate_code_region_table():

    for code in USA_AIRPORT_CODES:
        new_code_region = CodeRegion(code, "USA")
        db.session.add(new_code_region)



    db.session.commit()


def get_price(origin="SFO", destination="LHR", departure_date="2015-09-02", return_date="2015-09-16", max_price=2000):

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


def seed_response(response):

    outbound_flight_origin =
    outbound_flight _destination =
    outbound_airline =
    outbound_flight_number =
    outbound_datetime_departure =
    outbound_datetime_arrival =
    new_outbound_leg = FlightLeg(......)
    db.session.add(new_outbound_leg)
    db.session.commit()

    inbound_flight_origin =
    inbound_flight_destination =
    inbound_airline =
    inbound_flight_number =
    inbound_datetime_departure =
    inbound_datetime_arrival =
    new_inbound_leg = FlightLeg(......)
    db.session.add(new_inbound_leg)
    db.session.commit()

    base_fare = response['trips']['tripOption'][0]['pricing'][0]['saleFareTotal']
    taxes = response['trips']['tripOption'][0]['pricing'][0]['saleTaxTotal']
    total_fare = response['trips']['tripOption'][0]['pricing'][0]['saleTotal']

    if len(r['trips']['tripOption'][0]['slice'][0]['segment']) != 1:
     #the first leg of the trip only has 1 flight--origin_flight

    #the first leg of the trip has 2 flights---origin_flight and origin_connecting_flight

        outbound_connecting_flight_origin =
        outbound_connecting_flight _destination =
        outbound_connecting_airline =
        outbound_connecting_flight_number =
        outbound_connecting_datetime_departure =
        outbound_connecting_datetime_arrival =   
        new_outbound_connecting_leg = FlightLeg(......)
        db.session.add(new_outbound_connecting_leg)
        db.session.commit()

    else:
        new_outbound_connecting_leg = None
  
    

    if len(r['trips']['tripOption'][0]['slice'][1]['segment']) != 1:
        #the return leg of the trip only has 1 flight--return_flight
        #the return leg of the trip has 2 flights--return_flight and return_connecting_flight
      
        inbound_connecting_flight_origin =
        inbound_connecting_flight _destination =
        inbound_connecting_airline =
        inbound_connecting_flight_number =
        inbound_connecting_datetime_departure =
        inbound_connecting_datetime_arrival =
        new_inbound_connecting_leg = FlightLeg(......)
        db.session.add(new_inbound_connecting_leg)
        db.session.commit()

    else:
        new_inbound_connecting_leg = None

    code_region = CodeRegion.get(outbound_flight_origin).one()

    region = code_region.region

    flight = Flight(new_outbound_leg, new_outbound_connecting_leg, new_inbound_leg, new_inbound_connecting_leg, 
                    base_fare, taxes, total_fare)


    
    new_origin_leg = FlightLeg(origin_city_name, origin_airport_name, origin_airport_code, origin_airline,
                               origin_flight_number, origin_datetime_arrival, origin_datetime_departure)
    db.session.add(new_origin_leg)
    db.session.commit()

    new_return_leg = FlightLeg(return_city_name, return_airport_name, return_airport_code, return_airline,
                               return_flight_number, return_datetime_arrival, return_datetime_departure)
    db.session.add(new_return_leg)
    db.session.commit()

    if origin_connection_city_name:
        new_origin_connection_leg = FlightLeg(origin_connection_city_name, origin_connection_airport_name,
                                              origin_connection_airport_code, origin_connection_airline,
                                              origin_connection_flight_number, origin_connection_datetime_departure,
                                              origin_connection_datetime_arrival)
        db.session.add(new_origin_connection_leg)
        db.session.commit()
    else:
        new_origin_connection_leg = None

    if return_connection_city_name:
        new_return_connection_leg = FlightLeg(return_connection_city_name, return_connection_airport_name,
                                              return_connection_airport_code, return_connection_airline,
                                              return_connection_flight_number, return_connection_datetime_departure,
                                              return_connection_datetime_arrival)
        db.session.add(new_return_connection_leg)
        db.session.commit()
    else:
        new_return_connection_leg = None

    new_flight = Flight(new_origin_leg, new_origin_connection_leg, new_return_leg,
                        new_return_connection_leg, base_fare, taxes, total_fare, destination_region)
    db.session.add(new_flight)
    db.session.commit()


    for code in EUROPEAN_AIRPORT_CODES:  
      if code in EUROPEAN_AIRPORT_CODES:
        destination_region = "EUROPE"
    db.session.add(destination_region)
    db.session.commit()

    for code in AFRICAN_AIRPORT_CODES:  
      if code in AFRICAN_AIRPORT_CODES:
        destination_region = "AFRICA"
    db.session.add(destination_region)
    db.session.commit()

    for code in ASIAN_AIRPORT_CODES:
      if code in ASIAN_AIRPORT_CODES:
        destination_region = "ASIA"
    db.session.add(destination_region)
    db.session.commit()

    for code in MIDDLE_EASTERN_AIRPORT_CODES:
      if code in MIDDLE_EASTERN_AIRPORT_CODES:
        destination_region = "MIDDLE EAST"
    db.session.add(destination_region)
    db.session.commit()

    for code in LATIN_AMERICAN_AIRPORT_CODES: 
      if code in LATIN_AMERICAN_AIRPORT_CODES:
        destination_region = "LATIN AMERICA"
    db.session.add(destination_region)
    db.session.commit()

    for code in OCEANIAN_AIRPORT_CODES: 
      if code in OCEANIAN_AIRPORT_CODES:
        destination_region = "AUSTRALIA/PACIFIC"
    db.session.add(destination_region)
    db.session.commit()

    for code in MEXICO_CARIBBEAN_AIRPORT_CODES: 
      if code in MEXICO_CARIBBEAN_AIRPORT_CODES:
        destination_region = "MEXICO/CARIBBEAN"
    db.session.add(destination_region)
    db.session.commit()

    for code in USA_AIRPORT_CODES:  
      if code in USA_AIRPORT_CODES:
        destination_region = "USA"
    db.session.add(destination_region)
    db.session.commit()

    for code in CANADIAN_AIRPORT_CODES:  
      if code in CANADIAN_AIRPORT_CODES:
        destination_region = "CANADA"
    db.session.add(destination_region)
    db.session.commit()




if __name__ == "__main__":
  for city in CITY_COMBOS:
    data = get_price(city[0], city[1])
    seed_response(data)

    populate_code_region_table()
    get_price()





