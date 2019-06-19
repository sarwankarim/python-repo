print("**This is Marksheet Program**\n")

eng = int(input("Enter English Marks: "))
if eng < 0 or eng > 100:
	print("marks must be greater than 0 or less than 100")
	exit()

maths = int(input("Enter Maths Marks: "))
if maths < 0 or maths > 100:
	print("marks must be greater than 0 or less than 100")
	exit()

physics = int(input("Enter Physics Marks: "))
if physics < 0 or physics > 100:
	print("marks must be greater than 0 or less than 100")
	exit()

chem = int(input("Enter Chemistry Marks: "))
if chem < 0 or chem > 100:
	print("marks must be greater than 0 or less than 100")
	exit()

percentage = (eng + maths + physics + chem) / 4
print("\nPercentage: ", percentage,"%")	

if percentage >= 80 and percentage <= 100:
	print('Grade: ', 'A')
elif percentage >= 70 and percentage <= 79:
	print('Grade: ', 'A')
elif percentage >= 60 and percentage <= 69:
	print('Grade: ', 'B')
elif percentage >= 50 and percentage <= 59:
	print('Grade: ', 'C')
else:
	print('Grade: ', 'Fail')
	
def check_range(subject):
	if subject < 0 or subject > 100:
		print("marks must be greater than 0 or less than 100")
		exit()