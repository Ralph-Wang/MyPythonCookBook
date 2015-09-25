#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jsonschema import Draft4Validator

schema = {
    "items": {
        "anyOf": [
            {"type": "string", "maxLength": 2},
            {"type": "integer", "minimum": 5}
        ]
    }
}


instance = [{}, 3, "foo"]

v = Draft4Validator(schema)

errors = sorted(v.iter_errors(instance), key=lambda e: e.path)


for error in errors:
    for suberror in sorted(error.context, key=lambda e: e.schema_path):
        # sub message is in error.context
        print suberror.schema_path, suberror.message
    print "-" * 50
    print error # more infomation for debug
