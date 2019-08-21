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
	cssFile = open(inputFile + ".css", "r")
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
			
	newCssFile = open(outputFile + "-sorted" + ".css", "w")
	for key in sorted(dictOfLines):
		newCssFile.write(key)
		newCssFile.write(dictOfLines[key])
		
	newCssFile.close()
	cssFile.close()
	
if __name__ == "__main__":
	main(sys.argv[1:])