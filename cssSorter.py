# Run this script in the same directory of the css file
cssFileName = "testCss"
cssFile = open(cssFileName + ".css", "r")
lines = cssFile.readlines()
dictOfLines = { }
currentKey = ""
currentCssElement = ""
# Loop through the file and break it down into each element
for line in lines:
	# if there is a "{" we are at the start of a new element
	if "{" in line:
		#set up key in dict
		dictOfLines[line] = ""
		currentKey = line
	elif "}" in line:
		if "\n" not in line:
			line = line + "\n"
		currentCssElement += line
		dictOfLines[currentKey] = currentCssElement
		currentKey = ""
		currentCssElement = ""
	else:
		currentCssElement += line

		
newCssFile = open(cssFileName + "-sorted" + ".css", "w")
for key in sorted(dictOfLines):
	newCssFile.write(key)
	newCssFile.write(dictOfLines[key])
	print(key)
	
newCssFile.close()
cssFile.close()