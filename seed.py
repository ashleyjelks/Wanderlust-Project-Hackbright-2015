import urllib2
import json
import pprint
from model import connect_to_db, db, CodeRegion
from server import app



USA_AIRPORT_CODES = ['SFO', 'LAX', 'PHX', 'SEA', 'DEN', 'DFW', 'IAH', 'ORD',
                     'ATL', 'MIA', 'IAD', 'PHL', 'JFK', 'BOS', 'CLT', 'LAS']
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
CITY_COMBOS = [("SFO", "LAX"), ("SFO", "PHX"), ("SFO", "SEA"), ("SFO", "DEN"), ("SFO", "DFW"), ("SFO", "IAH"), ("SFO", "ORD"), ("SFO", "ATL"), ("SFO", "MIA")]
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
        print code
        usa = 'USA'
        print usa
        new_code_region = CodeRegion(code=code, region=usa)
        db.session.add(new_code_region)
    # db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    populate_code_region_table()
