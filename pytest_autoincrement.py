def incrementer(counter):
	return counter + 1


counter = 0

while counter < 5:
	print('This line should have an autoincrementing number', incrementer(counter))
	print('This line should have an autoincrementing number', incrementer(counter))
	print('This line should have an autoincrementing number', incrementer(counter))
	print('This line should have an autoincrementing number', incrementer(counter))
	counter += incrementer(counter)