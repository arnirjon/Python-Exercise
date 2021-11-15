#Find max number from the list

numbers = [4, 5, 9, 6]
max_num = numbers[0]


for i in numbers:

 if i > max_num:
	# 4 > 4 = f
	# 5 > 4 = t
	# 9 > 4 = t
	# ∵ The loop will be closed as the program finds the maximum number
   	max_num = i

	# ∵ The program will close when the program finds the maximum number
print(max_num)