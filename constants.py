# URL's
BASE_URI = "http://localhost:5000/ga4gh/drs/v1/objects/"
BASE_URI_STARTER_KIT = "http://localhost:4500/ga4gh/drs/v1/objects/"
ACCESS_ID_URI = "http://localhost:4500/ga4gh/drs/v1/stream/{object_id}/{access_id}"

# Data Objects
STARTER_KIT_OBJECTS = ["1a570e4e-2489-4218-9333-f65549495872","4d83ba3f-a476-4c7c-868f-3d1fcf77fe29","924901d5-6d31-4c33-b443-7931eadfac4b"]
SUCCESS_OBJECTS = ["8e18bfb64168994489bc9e7fda0acd4f","ecbb0b5131051c41f1c302287c13495c"]
FAILURE_OBJECT = ["xx18bfb64168994489bc9e7fda0acd4f"]
OBJECTS = SUCCESS_OBJECTS + FAILURE_OBJECT

# Headers
CONTENT_TYPE = "application/json"

# Schema
DRS_SCHEMA = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "string"},
        "name" : {"type" : "string"},
        "self_uri" : {"type" : "string"},
        "size" : {"type" : "number"},
        "created_time" : {"type" : "string"},
        "updated_time" : {"type" : "string"},
        "version" : {"type" : "string"},
        "mime_type" : {"type" : "string"},
        "description" : {"type" : "string"},
        "checksums": {"type" : "array"},
        "access_methods": {"type" : "array"},
        "aliases": {"type" : "array"},
        "contents": {"type" : "array"}
    },
    "required": ["id", "self_uri", "size", "created_time", "checksums"]
}

ERROR_SCHEMA = {
    "type":"object",
    "properties": {
        "error":"string",
        "msg":"string",
        "status_code":"number",
        "timestamp":"string",
    }
}
