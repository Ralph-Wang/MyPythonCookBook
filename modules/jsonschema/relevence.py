#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jsonschema import Draft4Validator
from jsonschema.exceptions import by_relevance, relevance

schema = {
    "properties": {
        "name": {"type": "string", "minLength": 3},
        "phones": {
            "type": "object",
            "properties": {
                "home": {"type": "string"}
            }
        }
    }
}

instance = {"name": "r", "phones": {"home": [123]}}

v = Draft4Validator(schema)

errors = list(v.iter_errors(instance))

print [e.validator for e in errors]
print [e.path[-1] for e in sorted(errors, key=relevance)]
print [e.validator for e in sorted(errors,
    key=by_relevance(weak=set(["type"]), strong=set(["minLength"])))]
