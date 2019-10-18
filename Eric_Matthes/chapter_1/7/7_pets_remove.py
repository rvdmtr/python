pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']

print(pets)

#while ('cat' and 'dog') in pets:
while 'cat' in pets:
	pets.remove('cat')
#	pets.remove('dog')
print(pets)