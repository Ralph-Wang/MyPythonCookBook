#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match

schema = {
    "type": "array",
    "items": {
        "type": "string",
    },
    "minItems": 3,
}

instance = [11]

v = Draft4Validator(schema)

errors = list(v.iter_errors(instance))

print best_match(errors).message

print "*" * 50

for error in errors:
    print error.path, error.message
