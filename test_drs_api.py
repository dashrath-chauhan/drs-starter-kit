import requests
import json
import unittest
import jsonschema
from jsonschema import validate
from . import constants

class TestDRS(unittest.TestCase):
    def print_request(self,request):
        print('\n{}\n{}'.format('-----------Request-----------',request.method + ' ' + request.url))

    def print_response(self,response):
        print('\n{}\n{}\n{}\n{}\n'.format(
            '-----------Response-----------',
            'Status Code:'+str(response.status_code),
            'Content Type:'+str(response.headers['Content-Type']),
            json.dumps(response.json()))
        )

    def test_success_status(self):
        for object_id in constants.SUCCESS_OBJECTS:
            url = constants.BASE_URI + object_id
            resp = requests.get(url)
            #self.print_request(resp.request)
            #self.print_response(resp)
            
            self.assertEqual(resp.status_code,200)
    
    def test_failure_status(self):
        for object_id in constants.FAILURE_OBJECT:
            url = constants.BASE_URI + object_id
            resp = requests.get(url)
            #self.print_request(resp.request)
            #self.print_response(resp)

            self.assertEqual(resp.status_code,404)
            self.assertNotEqual(resp.status_code,200)
            

    def test_content_type(self):
        for object_id in constants.OBJECTS:
            url = constants.BASE_URI + object_id
            resp = requests.get(url)
            #self.print_request(resp.request)
            #self.print_response(resp)
            
            self.assertEqual(resp.headers['Content-Type'],constants.CONTENT_TYPE)

    def test_success_schema(self):
        for object_id in constants.SUCCESS_OBJECTS:
            url = constants.BASE_URI + object_id
            resp = requests.get(url)
            json_response = resp.json()
            #self.print_request(resp.request)
            #self.print_response(resp)
            validate(instance=json_response, schema=constants.DRS_SCHEMA)

    def test_access_api_success_status(self):
        for object_id in constants.STARTER_KIT_OBJECTS:
            url = constants.BASE_URI_STARTER_KIT + object_id
            response = requests.get(url)
            response_body = response.json()
            access_id = response_body['access_methods'][0]['access_id']

            access_uri = constants.ACCESS_ID_URI.replace("{access_id}",access_id)
            access_uri = access_uri.replace("{object_id}",object_id)

            access_response = requests.get(access_uri)
            access_response_body = access_response.json()

            self.assertEqual(access_response.status_code,200)
            self.assertNotEqual(access_response.status_code,404)
        
if __name__ == '__main__':
   unittest.main()
