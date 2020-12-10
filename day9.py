
with open('input9.txt') as file:
	data = file.readlines()
	data = [ int(line.strip()) for line in data ]

def get_bad_number():

	for i in range(25, len(data)):
		preamble=data[i-25:i]
		num = data[i]
		found = False

		for j in range(len(preamble)-1):
			for k in range(j+1,len(preamble)):
				if preamble[j] + preamble[k] == num:
					found = True
					break
			if found == True:
				break

		if found == True:
			continue

		return num

num = get_bad_number()
print(num)

# part 2
def get_key():
	bad_num = get_bad_number()
	found = False

	for i in range(len(data)-1):
		nums = [data[i]]
		for j in range(i+1, len(data)):
			nums.append(data[j])

			if sum(nums) == bad_num:
				found = True
				break

			elif sum(nums) > bad_num:
				break

		if found == True:
			break

	return min(nums) + max(nums)

print(get_key())
