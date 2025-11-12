# Advanced quiz: ask capitals of 10 European countries.
def main():
	questions = [
		("France", "Paris"),
		("Germany", "Berlin"),
		("Italy", "Rome"),
		("Spain", "Madrid"),
		("United Kingdom", "London"),
		("Portugal", "Lisbon"),
		("Netherlands", "Amsterdam"),
		("Belgium", "Brussels"),
		("Switzerland", "Bern"),
		("Austria", "Vienna"),
	]
# heading
	print("European capitals quiz — 10 questions")
	print("Type your answer and press Enter. Answers are case-insensitive.\n")
# asigning the score
	score = 0
	for i, (country, capital) in enumerate(questions, start=1):
		answer = input(f"{i}. What is the capital of {country}? ").strip()

		# Case-insensitive comparison
		if answer.lower() == capital.lower():
			print("Correct!\n")
			score += 1
		else:
			print(f"Wrong. The correct answer is {capital}.\n")

	print(f"Quiz complete — you scored {score} out of {len(questions)}.")


if __name__ == "__main__":
	main()

