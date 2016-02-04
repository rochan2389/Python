
"""
Learning File - Reading files
If file is missing, Handle it with try and except

www.datagenx.net
"""

# In below example we are going to read a file 
# Below are the assumptions, 
# the file is existing in the code directory

file_name = raw_input("Enter the file name:- ")        # asking for the file name
try:
	fhand = open(file_name) 	# opening a handler or pointer for input file
except:
	print "File is not existing. Please try again"
	exit()
	
for line in fhand:                                     # reading each line from fhand
	print line										   # print
	
print "\nWe are done with file reading"
