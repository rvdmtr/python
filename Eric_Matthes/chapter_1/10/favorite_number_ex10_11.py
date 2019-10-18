#favorite_number.py
#10-11
import json

filename='txt_files/fav_num.json'

try:
	with open(filename) as f_obj:
		fav_num = json.load(f_obj)

except FileNotFoundError:
	fav = input('What is your favorite number? ')
	with open(filename,'w') as f_obj:
		json.dump(fav,f_obj)
else:
	print('I know you favorite number! It is ' + str(fav_num))