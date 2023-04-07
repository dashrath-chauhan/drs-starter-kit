import requests
import json
import jsonschema
from constants import *
import logging
logging.basicConfig(level=logging.INFO)

class CustomResponse:
    def __init__(self, object_id, test_name, result, message):
        self.object_id = object_id
        self.test_name = test_name
        self.result = result
        self.message = message

    def print_response(self):
        resp = {
            "object_id":self.object_id,
            "test_name":self.test_name,
            "pass":self.result,
            "message":self.message
        }
        
        print(resp)
        print('-----------------------------------------------')

def call_local_api(object_id):
    url = BASE_URI + object_id
    response = requests.get(url)
    return response

def call_drs_starter_kit_api(object_id):
    url = BASE_URI_STARTER_KIT + object_id
    response = requests.get(url)
    return response
    
def get_drs(object_id):
    if "-" in object_id:
        response = call_drs_starter_kit_api(object_id)
    else:
        response = call_local_api(object_id)
    response_body = response.json()

    if response.status_code == 200:
        result = True
        msg = response_body['description']
    else:
        result = False
        msg = response_body['msg']

    custom_response = CustomResponse(object_id, "GET_DRS_OBJECT_BY_ID", result, msg)
    custom_response.print_response()

def validate_drs_schema(response):
    if "-" in object_id:
        response = call_drs_starter_kit_api(object_id)
    else:
        response = call_local_api(object_id)
    response_body = response.json()

    #check if passed id is matching with self_uri
    if response.status_code == 200:
        self_uri_drs_id = response_body['self_uri'].split("/")[3]
        if self_uri_drs_id == object_id:
            result = True
            msg = "Return Object DRS_ID matched with passed object_id."
        else:
            result = False
            msg = "Return Object DRS_ID not match with passed object_id."
    else:
        result = False
        msg = response_body['msg']

    custom_response = CustomResponse(object_id, "TEST_OBJECT_ID_AND_RESPONSE_DRS_ID", result, msg)
    custom_response.print_response()

def access_id_validation(object_id):
    response = call_drs_starter_kit_api(object_id)
    response_body = response.json()
    access_id = response_body['access_methods'][0]['access_id']

    access_uri = ACCESS_ID_URI.replace("{access_id}",access_id)
    access_uri = access_uri.replace("{object_id}",object_id)

    response = requests.get(access_uri)
    response_body = response.json()

    if response.status_code == 200:
        result = True
        msg = "Generated access id uri is correct."
    else:
        result = False
        msg = "Generated access id uri is not correct."

    custom_response = CustomResponse(object_id, "ACCESS_ID_VALIDATION", result, msg)
    custom_response.print_response()
    
if __name__ == '__main__':
    logging.info("*****************LOCAL API test begins here*****************")
    for object_id in OBJECTS:
        get_drs(object_id)
    logging.info("*****************LOCAL API test ends here*****************")
    print("\n")
    logging.info("*****************DRS Validation test begins here*****************")
    for object_id in OBJECTS:
        validate_drs_schema(object_id)
    logging.info("*****************DRS Validation test ends here*****************")
    print("\n")
    logging.info("*****************STARTER KIT API test begins here*****************")
    for object_id in STARTER_KIT_OBJECTS:
        get_drs(object_id)
    logging.info("*****************STARTER KIT API test ends here*****************")
    print("\n")
    logging.info("*****************STARTER KIT DRS Validation test begins here*****************")
    for object_id in STARTER_KIT_OBJECTS:
        validate_drs_schema(object_id)
    logging.info("*****************STARTER KIT DRS Validation test ends here*****************")
    print("\n")
    logging.info("*****************ACCESS ID Validation test begins here*****************")
    for object_id in STARTER_KIT_OBJECTS:
        access_id_validation(object_id)
    logging.info("*****************ACCESS ID Validation test ends here*****************")
    
