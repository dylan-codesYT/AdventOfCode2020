
def get_unique_answers(response):
	questions = []

	for char in response:
		if char not in questions:
			questions.append(char)

	return len(questions)

with open('input6.txt') as file:
	data = file.readlines()
	data = [ line.strip() for line in data ]

sum = 0
currentResponse = ''
for line in data:
	if line != '':
		currentResponse += line

	else:
		sum += get_unique_answers(currentResponse)
		currentResponse = ''

sum += get_unique_answers(currentResponse)

print(sum)

# part 2

def get_unique_answer_all(responses):
	questions = []
	

	for char in responses[0]:
		inAllLines = True
		for line in responses:
			if char not in line:
				inAllLines = False

		if inAllLines and char not in questions:
			questions.append(char)

	return len(questions)

sum = 0
currentResponse = []
for line in data:
	if line != '':
		currentResponse.append(line)

	else:
		sum += get_unique_answer_all(currentResponse)
		currentResponse = []

sum += get_unique_answer_all(currentResponse)

print(sum)