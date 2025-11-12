# Check whether a number is even or odd.
# The program asks the user for a number from within main(), passes the value
def paritymessage(n: int) -> str:
	# Return a message saying whether n is even or odd.
	if n % 2 == 0:
		return f"{n} is even."
	else:
		return f"{n} is odd."

# function to get user input and display parity message
def main():
	user = input("Enter an integer: ").strip()
	try:
		value = int(user)
	except ValueError:
		print("Invalid input: please enter a whole integer (e.g. 4 or -3).")
		return
# get and print parity message
	msg = paritymessage(value)
	print(msg)
# entry point for the program
if __name__ == "__main__":
	main()

