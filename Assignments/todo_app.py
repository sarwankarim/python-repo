#TODO app
#pop each item after completion and append in empty list of completed_items

tasks = ['breakfast', 'quran', 'university', 'lunch', 'self studies', 'dinner', 'sleep']
print('All Tasks: ', format(tasks))

while tasks != []:
	task = input("Enter the task: ").lower()
	if task in tasks:
		tasks.pop(tasks.index(task))
		print("Remaining Tasks: ", format(tasks))
	else:
		print("Please enter correct task")

print("All Tasks has been completed.")