#!/bin/python

import uuid

def random_jsonId(function):
  def wrapper():
    jsonId = function()
    jsonId = jsonId + ".json"
    return jsonId
  return wrapper

@random_jsonId
def random_id():
  return str(uuid.uuid4())

