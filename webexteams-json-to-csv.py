#!/usr/bin/env python3

"""

Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

AUTHOR(S):  Vladimir Ivanovic <vivanovi@cisco.com>

"""


from __future__ import absolute_import, division, print_function

__author__ = "Vladimir Ivanovic <vivanovi@cisco.com>"
__contributors__ = []
__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"


# This script is meant for flattening Webex Teams Compliance JSON Data in to a CSV flat file

# Please ensure to use 'pip3 install flatten' to install the 'flatten' module
# More information here https://github.com/amirziai/flatten

# Please ensure to use 'pip3 install pandas' to install the 'pandas' module
# More information here https://github.com/pandas-dev/pandas

import csv
import json
from flatten_json import flatten
import pandas as pd
import numpy as np

# Define Function to be used iteratively over numerous JSON files
def flattenjson(a):

	# Open the JSON file
	with open(a, 'r') as b:

		# Convert JSON from STR to JSON Dictionary
		b = json.loads(b.read())
		
		# Use Flatten module on JSON, there are numerous JSON objects needing to be iterated through
		d = (flatten(c) for c in b)
		
		# Read Variable to Pandas
		df = pd.DataFrame(d)
		
		# Write Pandas DataFrame to CSV
		df.to_csv('test.csv')
		print("Successfully rewritten JSON to CSV!")

# Call flattenjson function + JSON File Name
flattenjson('c44f5690-6db9-11e6-8c7e-016ddef37535.json')		

indent = 4
print(
    __doc__,
    "Author:",
    " " * indent + __author__,
    "Contributors:",
    "\n".join([" " * indent + name for name in __contributors__]),
    "",
    __copyright__,
    "Licensed Under: " + __license__,
    sep="\n"
)