import re

names_file = open("names.txt", encoding = "utf-8")
data = names_file.read()
names_file.close()

first_name = r'Love'
last_name = r'Kenneth'

#print(re.match(first_name, data))
#print(re.search(last_name, data))

#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

#print(re.findall(r'\w*, \w+', data))

#(re.findall(r'[-\w\d+.]+@[-\w\d.]+',data))

#print(re.findall(r'\b[trehous]{9}\b', data, re.I))

#print(re.findall(r'''

#	\b@[-\w\d.]* #Find word bundary, an @, and then any numer of chars
#	[^gov\t]+ #Ignore one or more instances of the letters g, o,v and a tab
#	\b 	#Match another word boundary

#''',data, re.VERBOSE|re.I))

#print(re.findall(r'''
#	\b[-\w]+,
#	\s
#	[-\w ]+
#	[^\t\n]
#	''', data, re.X))

line = re.compile(r'''

	^(?P<name>(?P<last>[-\w ]*),(?P<first>\s[-\w ]+))\t
	(?P<email>[-\w\d.+]+@[-\w\d.]+)\t
	(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t
	(?P<job>[\w\s]+,\s[\w\s.]+)\t?
	(?P<twitter>@[\w\d]+)?$
	''', re.X|re.M)

#print(re.search(line, data).groupdict())

#print(line.search(data).groupdict())

for match in line.finditer(data):
	print("{first} {last} {email}".format(**match.groupdict()))
	print(match.group('name', 'email'))

