import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    dates = []
    colors = []
    
    for row in readCSV:
       color = row[3]
       date = row[0]

       dates.append(date)
       colors.append(color)

    print(dates)
    print(colors)

    whatColor = input('what color do you wish to know the date of?')
    coldex = colors.index(whatColor.lower())

    theDate = dates[coldex]

    print('the date of', whatColor, 'is:' , theDate)
