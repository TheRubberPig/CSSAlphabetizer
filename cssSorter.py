import sys, getopt

# Run this script in the same directory of the css file
def main(argv):
	inputFile = ""
	outputFile = ""
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
	except:
		print "cssSorter.py -i <inputfile> -o <outputfile>"
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print "cssSorter.py -i <inputfile> -o <outputfile>"
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputFile = arg
		elif opt in ("-o", "--ofile"):
			outputFile = arg
	processCss(inputFile, outputFile)
	
def processCss(inputFile, outputFile):
	dictOfLines = { }
	currentKey = ""
	currentCssElement = ""
	checkFileNames(inputFile, outputFile)
	try:
		cssFile = open(inputFile + ".css", "r")
	except:
		print("Could not find the file " + inputFile + ".css in the current directory.\nPlease ensure the spelling of the file name is correct")
		sys.exit(2)
	linesInCssFile = cssFile.readlines()
	for line in linesInCssFile:
		# if there is a "{" we are at the start of a new element
		if "{" in line:
			#set up key in dict
			dictOfLines[line] = ""
			currentKey = line
		elif "}" in line:
			# The last element in the file might not have a new line when inserted higher up in the file
			# This keeps the formatting consistent
			if "\n" not in line:
				line += "\n"
				
			currentCssElement += line
			dictOfLines[currentKey] = currentCssElement
			currentKey = ""
			currentCssElement = ""
		else:
			currentCssElement += line
			
	newCssFile = open(outputFile + ".css", "w")
	for key in sorted(dictOfLines):
		newCssFile.write(key)
		newCssFile.write(dictOfLines[key])
		
	print("New CSS file " + outputFile + ".css created!")
	newCssFile.close()
	cssFile.close()
	
def checkFileNames(inputFile, outputFile):
	if inputFile == "":
		print("Please provide an input file name\nUse the format cssSorter.py -i <inputfile> -o <outputfile>")
		sys.exit()
	elif outputFile == "":
		print("Please provide an output file name\nUse the format cssSorter.py -i <inputfile> -o <outputfile>")
		sys.exit()
	
	
if __name__ == "__main__":
	main(sys.argv[1:])