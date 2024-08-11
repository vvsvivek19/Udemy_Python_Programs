import csv

# Open the CSV file 'covid.csv' for writing. The 'newline' parameter is set to '' to prevent extra newlines on some platforms.
f = open('covid.csv', 'w', newline='')

# Create a CSV writer object to write data to the file
wrtr = csv.writer(f)

# Data to be written to the CSV file. Each tuple represents a row.
# The first tuple is the header row, and the subsequent tuples are data rows.
covid = [
    ('Country', 'Doses', 'People', 'Percentage'),  # Header row
    ('India', '186Cr', '84.1Cr', 61),  # Data row 1
    ('China', '330Cr', '124Cr', 88.1),  # Data row 2
    ('United States', '56.8Cr', '21.9Cr', 66.4),  # Data row 3
    ('Brazil', '42.4Cr', '16.2Cr', 76.4),  # Data row 4
    ('Indonesia', '39Cr', '16.2Cr', 59.3)  # Data row 5
]

# Loop through each tuple in the 'covid' list and write it to the CSV file
for t in covid:
    wrtr.writerow(t)

# Close the file to ensure all data is written and resources are released
f.close()

