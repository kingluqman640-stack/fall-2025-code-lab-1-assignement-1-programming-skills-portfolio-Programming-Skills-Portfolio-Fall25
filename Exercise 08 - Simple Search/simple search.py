# function to perform a simple search
def main():
	names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

	user_input = "Enter name to search for (press Enter to search for 'Sam'): "
	term = input(user_input).strip()
	if term == "":
		term = "Sam"

	# Perform a simple linear search and collect matching indices
	matches = [i for i, name in enumerate(names) if name == term]

	if matches:
		# Print first match and all indices
		print(f"'{term}' found at index(es): {', '.join(map(str, matches))}.")
	else:
		print(f"'{term}' not found in the list.")


if __name__ == "__main__":
	main()

