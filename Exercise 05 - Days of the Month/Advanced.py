# month -> days (February default 28)
def main():
	month_days = {
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
	user_input = input("Enter month number (1-12): ").strip()

	# Validate integer input
	try:
		month = int(user_input)
	except ValueError:
		print("Invalid input: please enter an integer between 1 and 12.")
		return

	# Use if-else to check validity and handle February leap-year adjustment
	if month in month_days:
		if month == 2:
			# Ask the user whether it's a leap year
			leap_answer = input("Is it a leap year? (yes/no): ").strip().lower()
			if leap_answer in ("yes", "y"):
				days = 29
			else:
				days = month_days[2]
		else:
			days = month_days[month]

		print(f"Month {month} has {days} days.")
	else:
		print("Invalid month number. Please enter a value from 1 to 12.")


if __name__ == "__main__":
	main()

