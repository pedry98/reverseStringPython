 
#pedritooo
#simple string reverse program for command line

string_inputstring = str(input("Please enter a string to reverse>> "))

def reverse_string(input):
	reversedstring = input[::-1]
	return reversedstring

newstring = reverse_string(string_inputstring)
print(newstring)	


answer = str(input("Wanna reverse more strings?").lower())
while answer == 'yes':
	string_inputstring = str(input("Please enter a string to reverse or type quit() to exit>> "))
	if string_inputstring == 'quit()':
		print('Have a nice day!!!')
		break
	else:
		newstring = reverse_string(string_inputstring)
		print(newstring)
if answer == 'no':
	print('Have a nice day!!!')







   


