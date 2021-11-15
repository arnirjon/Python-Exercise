#Find the largest among three numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))



# a = 12
# b = 45
# c = 34



if (a > b) and (a > c):

	max_number = a

elif (b > a) and (b > c):

	max_number = b

else:

	max_number = c

print("Maximum number is:", max_number)