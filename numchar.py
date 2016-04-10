#Prompts for an input string and then returns the input string
#along with the number of charcters in the string

inputString = ""
length = 0

while length == 0:	
	print ("Enter an input string:")
	inputString = str(input())
	length = len(inputString)

print ("{} has {} characters".format(inputString,length))