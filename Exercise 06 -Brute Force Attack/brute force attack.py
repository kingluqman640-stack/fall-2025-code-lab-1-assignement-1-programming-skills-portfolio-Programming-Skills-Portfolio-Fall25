# function to simulate a brute force password attack
def main():
	correctpassword = "12345"
	MAX_ATTEMPTS = 5  # set to None for unlimited attempts

	attempts = 0

	while True:
		# Prompt user
		attempt = input("Enter password: ").strip()

		# Check password
		if attempt == correctpassword:
			print("Password accepted. Access granted.")
			break

		# Wrong password
		attempts += 1
		# If a max attempts limit is set, show remaining attempts and potentially exit
		if MAX_ATTEMPTS is not None:
			remaining = MAX_ATTEMPTS - attempts
			if remaining > 0:
				print(f"Incorrect password. You have {remaining} attempts remaining.")
			else:
				print("Maximum attempts reached. Authorities have been alerted.")
				break
		else:
			# Unlimited attempts
			print("Incorrect password. Try again.")


if __name__ == "__main__":
	main()

