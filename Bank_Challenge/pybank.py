import csv
import statistics as stats

data = []
dataRevenue = []
totalMonths = 0
avgList = []
with open("budget_data.csv", 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	header = next(csvreader)
	for row in csvreader:
		data.append(row)
#print(data)
#set variable for first month of data Revenue to calculate change in months
previous_profit_loss = int(data[0][1])
for row in data:
	#created list of all values and casted as int to calculate sum of items.
	dataRevenue.append(int(row[1]))
	#getting the total counts of months in the data
	totalMonths += 1
	#getting the difference between months starting at month 2
	change = int(row[1]) - previous_profit_loss
	previous_profit_loss = int(row[1])
	#append each change in month to a list
	avgList.append(change)
#print(avgList)
#print(len(dataRevenue))
totalRevenue = sum(dataRevenue)
#taking the average of all values in the list
avgChange = round(stats.mean(avgList),2)
#taking the maximum and minimum numbers from the list.
greatIncrease = max(avgList)
greatDecrease = min(avgList)

# Find index location of the greatest increase and decrease to match index with data set.
for c,item in enumerate(avgList):
	if item == greatIncrease:
		positionIncrease = c
	elif item == greatDecrease:
		positionDecrease = c

''' data is a list of lists. data has a length of 41 items in the list. data [][] indicates
	each value of the 41 items. positionIncrease is the location of 1 of the 41 items in the data list.
	if positionIncrease is equal to 23, it will find the index of 23 and return data [][]. We then can
	find the month [0] and the revenue [1] from the data  '''
print(" ")
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total Revenue: ${totalRevenue}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {data[positionIncrease][0]} ${greatIncrease}")
print(f"Greatest Decrease in Profits: {data[positionDecrease][0]} ${greatDecrease}")

new_file = open("new_file.txt", 'w')
new_file.write("Financial Analysis" + '\n')
new_file.write("-----------------------------" + '\n')
new_file.write(f"Total Months: {totalMonths}" + '\n')
new_file.write(f"Total Revenue: ${totalRevenue}" + '\n')
new_file.write(f"Average Change: ${avgChange}" + '\n')
new_file.write(f"Greatest Increase in Profits: {data[positionIncrease][0]} ${greatIncrease}" + '\n')
new_file.write(f"Greatest Decrease in Profits: {data[positionDecrease][0]} ${greatDecrease}")
new_file.close()
