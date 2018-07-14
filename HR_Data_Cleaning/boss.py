import csv
import datetime
#imported another python file with a dictionary of states
import usabbrev


data = []
with open("employee_data.csv", 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	header = next(csvreader)
	for row in csvreader:
		data.append(row)
states =[]
for key,value in usabbrev.us_state_abbrev.items():
	states.append(value)

emplID = []
first_name = []
last_name = []
birthdate = []
SSN = []
state = []

for row in data:
	emplID.append(row[0])
	full_name = row[1].split(" ")
	first_name.append(full_name[0])
	last_name.append(full_name[1])
	d = datetime.datetime.strptime(row[2], '%Y-%m-%d')
	date = datetime.date.strftime(d, '%m-%d-%y')
	birthdate.append(date)
	SSN.append("***-**-" + row[3][7:11])
	US = row[4]
	for key,value in usabbrev.us_state_abbrev.items():
		if key == US:
			state.append(value)

newData = zip(emplID,first_name,last_name,birthdate,SSN,state)


output = ("employee_data_cleaned.csv")
with open(output,'w') as datafile:
	csvwriter = csv.writer(datafile)
	csvwriter.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"])
	csvwriter.writerows(newData)


