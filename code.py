import csv

results = []
count = 1
EURO_TO_USD = 0.88

# Get user input
user_input = input("Enter a name or part of a name: ")
print("\n")

# Get the player's information
with open('players_20.csv', 'r', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        if user_input in row[3]:
        	print("PLAYER #" + str(count) + "\n==================================================================================")

        	print(f'{"Full name: ":50} {row[3]}')
        	print(f'{"Nationality: ":50} {row[8]}')
        	print(f'{"Club: ":50} {row[9]}')
        	print(f'{"Date of birth: ":50} {row[5]}')
        	print(f'{"Age: ":50} {row[4]}')
        	print(f'{"Contract expires on: ":50} {row[28]}')
        	print(f'{"Difference of actual vs. potential score: ":50} {str(int(row[10]) - int(row[11]))}')
        	
        	if type(row[22]) == int:
        		print(f'{"Amount to pay for player release: ":50} {"${:,.2f}".format(float(row[22]) * EURO_TO_USD)}')

        	print(f'{"Value: ":50} {"${:,.2f}".format(float(row[12]) * EURO_TO_USD)}')
        	print(f'{"Salary: ":50} {"${:,.2f}".format(float(row[13]) * EURO_TO_USD)}')
        	print(f'{"Traits: ":50} {row[43]}')

        	print("\n")

        	count += 1

