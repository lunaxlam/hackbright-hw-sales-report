"""Generate sales report showing total melons each salesperson sold. Note: Suggested revision of sales_report.py"""

import sys

# Get name of report .txt and create file object
get_file = f'{sys.argv[1]}'
f = open(get_file)

# Initialize a dictionary of salesperson, number of melons (key, value) pairs
sales_summary = {}

# Iterate over each line in the file object
for line in f:
    # Remove any whitespace to the right of each line
    line = line.rstrip()
    # Store each line into a list variable, using the pipe symbol as a delimiter
    entries = line.split('|')
    # Store the name of the salesperson by accessing the 0th index of the entries list
    salesperson = entries[0]
    # Store the number of elements by accessing the 2th index of the entries list and casting it as an integer type 
    melons = int(entries[2])

    # Add salesperson and number of melons sold to the dictionary
    sales_summary[salesperson] = melons

# Iterate through each element in dictionary
for salesperson, melons in sales_summary.items():
    # Print message
    print(f'{salesperson} sold {melons} melons.')