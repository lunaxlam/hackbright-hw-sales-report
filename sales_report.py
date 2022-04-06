"""Generate sales report showing total melons each salesperson sold."""

# Initialize a list of all the salespeople
salespeople = []

# Initialize a list of all the melons old
melons_sold = []

# Create a file object of the given .txt file
f = open('sales-report.txt')

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

    # Check to see if salesperson from the read line in the file already exists in the salespeople list
    if salesperson in salespeople:
        # If so then get the index of the salesperson in the salespeople list and store the index value in position
        position = salespeople.index(salesperson)
        # Update the number of melons sold at that particular index in melons_sold
        melons_sold[position] += melons
        
    else:
        # Otherwise, add the salesperson to the salespeople list
        salespeople.append(salesperson)
        # Add the number of melonsn the salesperson sold to melons
        melons_sold.append(melons)

# Iterate through each element in salespeople
for i in range(len(salespeople)):
    # Print message
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')