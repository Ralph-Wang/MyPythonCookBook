#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jsonschema import validate


schema = {
        "type": "object",
        "additionalProperties": False,
        "properties":{
            "price": {"type": "number"},
            "name": {"type": "string"}
            }
        }

validate({"name": "Eggs", "price": 34.99, "addition": []}, schema)
