import Sample_Python_JSON_API_Call_Code
from Sample_Python_JSON_API_Call_Code import response

import json 


parsed_json = json.loads(response)

print parsed_json.keys()
print parsed_json.items()

