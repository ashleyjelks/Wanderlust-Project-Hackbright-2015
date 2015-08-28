import urllib2import sysimport jsonimport pprintimport dateutil.parserfrom model import connect_to_db, db, Flight, User, Search, SavedSearchfrom server import appfrom airline_airport_conversions import airlines, cities, airportsfrom time import sleep# from key import google_flights_api_key_1, google_flights_api_key_2, google_flights_api_key_3, google_flights_api_key_4, google_flights_api_key_5, google_flights_api_key_6API_URL = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCCAL7u_3hy7OTFiMcPXydkfwFR_WwTZN0"USA_AIRPORT_CODES = ["SFO", "LAX", "PHX", "SEA", "DEN", "DFW", "ORD", "ATL", "MIA", "IAD", "JFK", "BOS", "LAS", "OGG"]BROKEN_DOMESTIC_CITIES = [("JFK", "PHX"), ("BOS", "PHX"), ("BOS", "ATL"),("ATL", "PHX"), ("ATL", "BOS"), ("ATL", "JFK"), ("DFW", "JFK"), ("MIA", "PHX"), ("MIA", "SEA"), ("PHX", "MIA"),  ("PHX", "ATL"),  ]BROKEN_INTL_CITIES = [("SFO", "MBJ"),("SFO", "LHR"), ("SFO", "FCO"), ("LAX", "EZE"), ("LAX", "SYD"), ("SEA", "YYZ"), ("SEA", "LHR"), ("DEN", "YVR"), ("DFW", "CDG"),("ORD", "MAD"), ("ORD", "DUB"), ("ATL", "LHR"), ("MIA", "MAD"), ("MIA", "CDG"), ("IAD", "CUN"), ("IAD", "LHR"), ("IAD", "DUB"), ("BOS", "LHR"), ("LAS", "YYZ"), ]PHX_AIRPORT_CODES = [("PHX", "IAD"), ("PHX", "BOS"), ("PHX", "LAS"), ("PHX", "OGG"), ("PHX", "JFK")]SFO_AIRPORT_CODES = [("SFO", "LAX"), ("SFO", "PHX"), ("SFO", "SEA"), ("SFO", "DEN"), ("SFO", "DFW"), ("SFO", "ORD"), ("SFO", "ATL"), ("SFO", "MIA"), ("SFO", "IAD"), ("SFO", "BOS"), ("SFO", "LAS"), ("SFO", "OGG"), ("SFO", "JFK")]SEA_AIRPORT_CODES = [("SEA", "SFO"), ("SEA", "LAX"), ("SEA", "PHX"), ("SEA", "DEN"), ("SEA", "DFW"), ("SEA", "ORD"), ("SEA", "ATL"), ("SEA", "MIA"), ("SEA", "IAD"), ("SEA", "BOS"), ("SEA", "LAS"), ("SEA", "OGG"), ("SEA", "JFK")]IAD_AIRPORT_CODES = [("IAD", "SFO"), ("IAD", "LAX"), ("IAD", "PHX"), ("IAD", "SEA"), ("IAD", "DEN"), ("IAD", "DFW"), ("IAD", "ORD"), ("IAD", "ATL"), ("IAD", "MIA"), ("IAD", "BOS"), ("IAD", "LAS"), ("IAD", "OGG"), ("IAD", "JFK")]"""Select statements to locate flights with dirty data:SELECT * FROM  FLIGHTS where outbound_city_origin is NOT inbound_city_final_destination;SELECT * FROM  FLIGHTS where inbound_city_origin is NOT outbound_city_final_destination;"""def get_price(first_origin, destination):    flight_request = {        "request": {            "passengers": {                "kind": "qpxexpress#passengerCounts",                "adultCount": 1,            },            "slice": [                {                    "kind": "qpxexpress#sliceInput",                    "origin": first_origin,                    "destination":  destination,                    "date": "2015-09-02",                    "maxStops": 1,                    "maxPrice": 3000                },                {                    "kind": "qpxexpress#sliceInput",                    "origin": destination,                    "destination": first_origin,                    "date": "2015-09-16",                    "maxStops": 1,                    "maxPrice": 3000                }            ],            "refundable": "false",            "solutions": 1        }    }    jsonreq = json.dumps(flight_request, encoding='utf-8', indent=1)    try:        req = urllib2.Request(API_URL, jsonreq, {'Content-Type': 'application/json'})        flight = urllib2.urlopen(req)        response = flight.read()        flight.close()        parsed_json = json.loads(response)        printer = pprint.PrettyPrinter()        printer.pprint(parsed_json)        response = parsed_json        if len(response['trips']['tripOption'][0]['slice'][0]['segment']) == 1:            outbound_city_final_destination = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['destination']            outbound_destination_city_airport = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['destination']            inbound_city_final_destination = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['destination']            inbound_destination_city_airport = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['destination']            outbound_datetime_arrival = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['arrivalTime'])            inbound_datetime_arrival = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['arrivalTime'])        else:            outbound_city_final_destination = response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['destination']            inbound_city_final_destination = response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['destination']            outbound_datetime_arrival = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][0]['segment'][1]['leg'][0]['arrivalTime'])            inbound_datetime_arrival = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][1]['segment'][1]['leg'][0]['arrivalTime'])        outbound_city_origin = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['origin']        outbound_city_airport = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['origin']        outbound_airline_code = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['carrier']        outbound_flight_number = response['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['number']        outbound_datetime_departure = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['departureTime'])        inbound_city_origin = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['origin']        inbound_city_airport = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['origin']        inbound_airline_code = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['carrier']        inbound_flight_number = response['trips']['tripOption'][0]['slice'][1]['segment'][0]['flight']['number']        inbound_datetime_departure = dateutil.parser.parse(response['trips']['tripOption'][0]['slice'][1]['segment'][0]['leg'][0]['departureTime'])        base_fare = response['trips']['tripOption'][0]['pricing'][0]['saleFareTotal']        base_fare = base_fare[3:]        base_fare = float(base_fare)        base_fare = int(base_fare)        taxes = response['trips']['tripOption'][0]['pricing'][0]['saleTaxTotal']        taxes = taxes[3:]        taxes = float(taxes)        taxes = int(taxes)        total_fare = response['trips']['tripOption'][0]['pricing'][0]['saleTotal']        total_fare = total_fare[3:]        total_fare = float(total_fare)        total_fare = int(total_fare)        outbound_datetime_departure = str(outbound_datetime_departure)        outbound_datetime_arrival = str(outbound_datetime_arrival)        inbound_datetime_departure = str(inbound_datetime_departure)        inbound_datetime_arrival = str(inbound_datetime_arrival)        outbound_datetime_departure = outbound_datetime_departure[0:16]        outbound_datetime_arrival = outbound_datetime_arrival[0:16]        inbound_datetime_departure = inbound_datetime_departure[0:16]        inbound_datetime_arrival = inbound_datetime_arrival[0:16]        outbound_airline_name = airlines[outbound_airline_code]        inbound_airline_name = airlines[inbound_airline_code]        outbound_city_origin = cities[outbound_city_origin]        inbound_city_origin = cities[inbound_city_origin]        outbound_city_final_destination = cities[outbound_city_final_destination]        inbound_city_final_destination = cities[inbound_city_final_destination]        outbound_city_airport = airports[outbound_city_airport]        inbound_city_airport = airports[inbound_city_airport]        flight = Flight(outbound_city_origin=outbound_city_origin, outbound_city_final_destination=outbound_city_final_destination, outbound_airline_code=outbound_airline_code, outbound_airline_name=outbound_airline_name, outbound_flight_number=outbound_flight_number, outbound_datetime_departure=outbound_datetime_departure, outbound_datetime_arrival=outbound_datetime_arrival, inbound_city_origin=inbound_city_origin, inbound_city_final_destination=inbound_city_final_destination, inbound_airline_code=inbound_airline_code, inbound_airline_name=inbound_airline_name, inbound_flight_number=inbound_flight_number, inbound_datetime_departure=inbound_datetime_departure, inbound_datetime_arrival=inbound_datetime_arrival, outbound_city_airport=outbound_city_airport, inbound_city_airport=inbound_city_airport, base_fare=base_fare, taxes=taxes, total_fare=total_fare)        db.session.add(flight)        db.session.commit()    except urllib2.HTTPError as e:        print "There was an urllib2.HTTPError...API RATE LIMIT REACHED !!!!!!!!!!"        return flightif __name__ == "__main__":    connect_to_db(app)    for city in PHX_AIRPORT_CODES:        get_price(city[0], city[1])