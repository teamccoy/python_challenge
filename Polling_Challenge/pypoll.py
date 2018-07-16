import csv

data = []

with open("election_data.csv", 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	header = next(csvreader)
	for row in csvreader:
		data.append(row)

totalVotes = 0
totalKhan = 0
totalCorrey = 0
totalLi = 0
totalOTooley = 0

#print(data[0:10])

for row in data:
	totalVotes += 1
	if row[2] == "Khan":
		totalKhan += 1
	elif row[2] == "Correy":
		totalCorrey += 1
	elif row[2] == "O'Tooley":
		totalOTooley += 1
	elif row[2] == "Li":
		totalLi += 1
percentageKhan = round((totalKhan/totalVotes)*100,2)
percentageCorrey = round((totalCorrey/totalVotes)*100,2)
percentageLi = round((totalLi/totalVotes)*100,2)
percentageOTooley = round((totalOTooley/totalVotes)*100,2)

winner = max(percentageOTooley,percentageLi,percentageCorrey,percentageKhan)
#data format is voterID, County, Candidate
#print(totalVotes)
#print(totalKhan)
if winner == percentageKhan:
	poll_winner = "Khan"
elif winner == percentageCorrey:
	poll_winner = "Correy"
elif winner == percentageLi:
	poll_winner = "Li"
elif winner == percentageOTooley:
	poll_winner = "O'Tooley"

print(" ")
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {totalVotes}")
print("-----------------------------")
print(f"Khan: {percentageKhan}% ({totalKhan})")
print(f"Correy: {percentageCorrey}% ({totalCorrey})")
print(f"Li: {percentageLi}% ({totalLi})")
print(f"O'Tooley: {percentageOTooley}% ({totalOTooley})")
print("-----------------------------")
print(f"Winner: {poll_winner}")
print("-----------------------------")


new_file = open("pypoll.text", 'w')
new_file.write("Election Results")
new_file.write("-----------------------------")
new_file.write(f"Total Votes: {totalVotes}")
new_file.write("-----------------------------")
new_file.write(f"Khan: {percentageKhan}% ({totalKhan})")
new_file.write(f"Correy: {percentageCorrey}% ({totalCorrey})")
new_file.write(f"Li: {percentageLi}% ({totalLi})")
new_file.write(f"O'Tooley: {percentageOTooley}% ({totalOTooley})")
new_file.write("-----------------------------")
new_file.write(f"Winner: {poll_winner}")
new_file.write("-----------------------------")
new_file.close
