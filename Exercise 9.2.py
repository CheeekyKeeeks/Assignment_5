>>> def has_no_e(word):
... 	for letter in word:
...        	if letter == 'e':
...            		return False
...    	return True
>>>
>>> fin = open('C:\$\Grad School\GIS6345 - Geospatial Programming\Week 5\words.txt')
>>> count = 0
>>> num_of_words = 113809
>>>
>>> for line in fin:
...	word = line.strip()
...     if has_no_e(word) == True:
...		count += 1
... 		print(word)
>>>