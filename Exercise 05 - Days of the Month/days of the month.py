# Dictionary: month number -> days (February set to 28 by default)
def main():
	daysofthemonth = {
		1: 31,
		2: 28,
		3: 31,
		4: 30,
		5: 31,
		6: 30,
		7: 31,
		8: 31,
		9: 30,
		10: 31,
		11: 30,
		12: 31,
	}
# declaring variable for user input
	userinput = input("Enter month number (1-12): ").strip()

	# Validate integer input
	try:
		month = int(userinput)
	except ValueError:
		print("Invalid input: please enter an integer between 1 and 12.")
		return

	# Check and output using if-else
	if month in daysofthemonth:
		days = daysofthemonth[month]
		print(f"Month {month} has {days} days.")
	else:
		print("Invalid month number. Please enter a value from 1 to 12.")


if __name__ == "__main__":
	main()

