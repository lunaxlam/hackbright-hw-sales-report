"""Generate sales report showing total melons each salesperson sold. Note: Suggested revision of sales_report.py"""

import sys


def open_file(file):
    """Open a file and return a file object to iterate through."""

    file = open(file)

    return file


def get_melon_sales(file):
    """Iterate through a sales report file to return a dictionary (salesperson: number of melons) key, value pairs."""

    # Initialize a dictionary of salesperson, number of melons (key, value) pairs
    sales_summary = {}

    # Iterate over each line in the file object
    for line in file:
        # Remove any whitespace to the right of each line
        line = line.rstrip()
        # Store each line into a list variable, using the pipe symbol as a delimiter
        salesperson, total_sales, melons_sold = line.split('|')

        # Add salesperson and number of melons sold to the dictionary
        if salesperson in sales_summary:
            sales_summary[salesperson] += int(melons_sold)
        else:
            sales_summary[salesperson] = int(melons_sold)
    
    return sales_summary


def print_melon_report(sales_summary, file):
    """Print melon sales report summary."""

    # Iterate through each element in dictionary
    for salesperson, melons_sold in sales_summary.items():
        # Print message
        print(f'{salesperson} sold {melons_sold} melons.')


# Get a file as a string from the command line
f = sys.argv[1]

# Open the file
file = open_file(f)

# Generate sales info
sales_summary = get_melon_sales(file)

# Print message
print(print_melon_report(sales_summary, file))

# Close the file
file.close()
