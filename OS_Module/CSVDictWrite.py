import csv

f = open('Covid_CSV_Dict.csv','w',newline='')

covid = [
    {'Country': 'India', 'Doses': '186Cr', 'People': '84.1Cr', 'Percentage': '61'}, 
    {'Country': 'China', 'Doses': '330Cr', 'People': '124Cr', 'Percentage': '88.1'}, 
    {'Country': 'United States', 'Doses': '56.8Cr', 'People': '21.9Cr', 'Percentage': '66.4'}, 
    {'Country': 'Brazil', 'Doses': '42.4Cr', 'People': '16.2Cr', 'Percentage': '76.4'}, 
    {'Country': 'Indonesia', 'Doses': '39Cr', 'People': '16.2Cr', 'Percentage': '59.3'}
    ]

fields = ['Country','Doses','People','Percentage']

wrtr = csv.DictWriter(f,fields)

wrtr.writeheader()

for d in covid:
    wrtr.writerow(d)

f.close()

