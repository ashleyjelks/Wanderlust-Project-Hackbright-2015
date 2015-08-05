# from google.appengine.ext import vendor

# # Add any libraries installed in the "lib" folder.

# vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))

[( 'kind',  'qpxExpress#tripsSearch'), 

( 'trips', 
    { 'tripOption': [{ 'saleTotal':  'USD97.10', 

     'kind':  'qpxexpress#tripOption', 
    
     'slice': 

        [{ 'duration': 101,  'kind':  'qpxexpress#sliceInfo',  'segment': 
       
        [{
         'kind':  'qpxexpress#segmentInfo',
         'bookingCodeCount': 7, 
         'flight': { 'carrier':  'AS',  'number':  '247'}, 
        
         'leg':[{
         'origin':  'SFO',  'originTerminal':  'I', 
         'departureTime':  '2015-11-20T20:25-08:00',
         'onTimePerformance': 100, 
         'secure': True,
         'destination':  'PDX', 

         'kind':  'qpxexpress#legInfo', 
         'meal':  'Food for Purchase', 
         'aircraft':  '734', 
         'mileage': 550, 
         'arrivalTime':  '2015-11-20T22:06-08:00', 
         'duration': 101, 
         'id':  'LY1h+LKRaj+ZjNqS'
        }], 

         'bookingCode':  'G', 
         'duration': 101, 
         'id':  'GOgSHLJ3K56UA4bV', 
         'cabin':  'COACH', 
         'marriedSegmentGroup':  '0'
        }]}], 

         'id':  'evfa5U0rmf8MNpH5ptFnf4001', 
        
         'pricing': [{ 'fare': [{ 'origin':  'SFO',  'basisCode':  'G14VN5', 
         'kind':  'qpxexpress#fareInfo', 
             'destination':  'PDX', 
             'carrier':  'AS', 
             'id':  'AW7+jtYes6lxOYwsoJhKNUwpC/lD7oguAk+b5Ztaom+s'}], 
            
         'saleTotal':  'USD97.10', 
         'kind':  'qpxexpress#pricingInfo', 
        
         'segmentPricing': 
        
        [{ 'kind':  'qpxexpress#segmentPricing',
             'fareId':  'AW7+jtYes6lxOYwsoJhKNUwpC/lD7oguAk+b5Ztaom+s',
             'freeBaggageOption': [{ 'kind':  'qpxexpress#freeBaggageAllowance',  'pieces': 0}], 
             'segmentId':  'GOgSHLJ3K56UA4bV'}], 
       
     'passengers': 
    { 'kind':  'qpxexpress#passengerCounts',  'adultCount': 1}, 


     'ptc':  'ADT', 

     'tax': 

        [{ 'kind':  'qpxexpress#taxInfo', 
             'code':  'US', 
             'country':  'US', 
             'salePrice':  'USD5.79',
             'chargeType':  'GOVERNMENT', 
             'id':  'US_001'}, 
    
    { 'kind':  'qpxexpress#taxInfo', 
         'code':  'AY',
         'country':  'US', 
         'salePrice':  'USD5.60', 
         'chargeType':  'GOVERNMENT', 
         'id':  'AY_001'}, 
                

    { 'kind':  'qpxexpress#taxInfo', 
         'code':  'XF', 
         'country':  'US', 
         'salePrice':  'USD4.50', 
         'chargeType':  'GOVERNMENT', 
         'id':  'XF'},

    { 'kind':  'qpxexpress#taxInfo', 
         'code':  'ZP', 
         'country':  'US', 
         'salePrice':  'USD4.00', 
         'chargeType':  'GOVERNMENT',
         'id':  'ZP'
    }], 
        
     'fareCalculation': 
     'SFO AS PDX 77.21G14VN5 USD 77.21 END ZP SFO XT 5.79US 4.00ZP 5.60AY 4.50XF SFO4.50', 
     'saleFareTotal':  'USD77.21',
     'baseFareTotal':  'USD77.21',
     'saleTaxTotal':  'USD19.89', 

     'latestTicketingTime': 
     '2015-08-05T23:59-04:00'}]}], 

     'kind':  'qpxexpress#tripOptions', 
    
     'data': 
    { 'city': 
        [{ 'kind':  'qpxexpress#cityData', 'code':  'PDX', 'name':  'Portland'}, 
        { 'kind':  'qpxexpress#cityData', 'code':  'SFO', 'name':  'San Francisco'}], 
    
    'kind':  'qpxexpress#data', 
    
    'tax': [{ 'kind':  'qpxexpress#taxData',  'id':  'ZP',  'name':  'US Flight Segment Tax'}, 
            { 'kind':  'qpxexpress#taxData',  'id':  'AY_001',  'name':  'US September 11th Security Fee'}, 
            { 'kind':  'qpxexpress#taxData', 'id':  'US_001',  'name':  'US Transportation Tax'}, 
            { 'kind':  'qpxexpress#taxData',  'id':  'XF',  'name':  'US Passenger Facility Charge'}], 

    'airport': [{ 'city':  'PDX',  'kind':  'qpxexpress#airportData',  'code':  'PDX',  'name':  'Portland International'}, 
                { 'city':  'SFO',  'kind':  'qpxexpress#airportData',  'code':  'SFO',  'name':  'San Francisco International'}], 

    'aircraft': [{ 'kind':  'qpxexpress#aircraftData',  'code':  '734',  'name':  'Boeing 737'}], 

    'carrier': [{ 'kind':  'qpxexpress#carrierData',  'code':  'AS',  'name':  'Alaska Airlines Inc.'}]},

    'requestId':  'rFK5DeEDXVsBvaeNe0McSB'})]


















