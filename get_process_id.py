#!/usr/bin/python3

import sys
from json import loads

def get_process_id(PFile):
    ihub_data = loads(PFile)
    return ihub_data['processId']

print(get_process_id(sys.argv[1]))