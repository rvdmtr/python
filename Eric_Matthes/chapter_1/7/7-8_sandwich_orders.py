sandwich_orders = ['jorgo','cheesetta','mushroomium']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made you ' + sandwich.title() + ' sandwich.')
	finished_sandwiches.append(sandwich)

print('\nWe made some delicious sandwiches, here they are: ')
for sw in finished_sandwiches:
	print('\t' + sw.title() + ' sandwich')

print('\n\n##########################')
print('##########################\n')
####
#### 7-9 without pastrami
####


sandwich_orders = ['jorgo','pastrami','cheesetta','pastrami','mushroomium','pastrami']
finished_sandwiches = []

print('--- We are sorry, but pastrami sandwich is not available for order ---\n')
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made you ' + sandwich.title() + ' sandwich.')
	finished_sandwiches.append(sandwich)

print('\nWe made some delicious sandwiches, here they are: ')
for sw in finished_sandwiches:
	print('\t' + sw.title() + ' sandwich')