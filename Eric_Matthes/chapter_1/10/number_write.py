#number_writer.py

import json

numbers = [2,3,5,7,9,11,13]

filename = 'txt_files/numbers.json'

with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)


