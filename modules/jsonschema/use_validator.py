#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jsonschema


schema = {
        "type": "object",
        "additionalProperties": False,
        "properties":{
            "price": {"type": "number"},
            "name": {"type": "string"}
            }
        }

# validator = jsonschema.Draft3Validator(schema)
validator = jsonschema.Draft4Validator(schema)

obj = {"name": "box", "price": "25", "owner": "ralph"}

print validator.is_valid(obj)
print validator.is_type(obj, "object")

for error in validator.iter_errors(obj):
    print repr(error)

