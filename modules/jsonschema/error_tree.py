#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jsonschema import Draft4Validator, ErrorTree

schema = {
    "type": "array",
    "items": {"type": "number", "enum": [1, 2, 3]},
    "minItems": 3,
}

instance = ["spam", 2]

v = Draft4Validator(schema)

# for error in sorted(v.iter_errors(instance), key=str):
#     print error.message

tree = ErrorTree(v.iter_errors(instance))

# 0 and 1 notes the path in the instance
print 0 in tree
print 1 in tree

# index the tree to find out errors
print sorted(tree[0].errors)

# then index the errors
print tree[0].errors["type"].message
print tree[0].errors["enum"].message

# check error type as well
print "enum" in tree[0].errors
print "minimun" in tree[0].errors

# global error in the tree
print "minItems" in tree.errors
print tree.errors["minItems"].message
