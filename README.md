# drs-starter-kit
This projects is specifically developed with regards to coding assesment of EMBL-EBI. Do not share or use this project without EMBL-EBI's consent.

## Overview
This repository consists of a solution file to EMBL coding assessment. 
- There are three **.py** files.
1. **tech_test_solution.py** includes code to access DRS API and perform some test as mentioned in requirement document.
2. **test_drs_api.py** includes few test cases on DRS API.
3. **constants.py** includes few constant variables used in above files.

## Tasks
- Mandatory tasks:
- In this solution, I am using two DRS containers that runs on localhost port 5000 which includes `object_id` given in request document.
- Container running on port 4500 includes `object_id` from **GA4GH Starter Kit DRS website:** https://starterkit.ga4gh.org/docs/starter-kit-apis/drs/drs_overview.
1. Using Python, send a `GET` request to `http://localhost:5000/ga4gh/drs/v1/objects/{object_id}` endpoint with the below listed input DRS object Ids and verify that the outputs are as expected:

|object_id | Expected Status Code | Expected Content Type |
| -------- | -------------------- | --------------------- |
|8e18bfb64168994489bc9e7fda0acd4f  | 200 | JSON |
|ecbb0b5131051c41f1c302287c13495c  | 200 | JSON |
|xx18bfb64168994489bc9e7fda0acd4f  | 404 | JSON |

- Additional tasks:
1. DRS Schema validation according to DRS v1.2 specification
2. Access method API `http://localhost:4500/ga4gh/drs/v1/stream/{object_id}/{access_id}` validation based on response received after submitting `GET` request to `http://localhost:4500/ga4gh/drs/v1/objects/{object_id}`.

## Installation
To install prerequisite before running the project run the command:
```
pip3 install -r requirements.txt
```

## Usage
To run the solution for task use command:
```
python .\tech_test_solution.py
```
To run tests use command:
```
pytest .\test_drs_api.py -v
```