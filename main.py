VRanks = ['S', 'S-', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D']

r = 0
infilepath = 'import.txt'
filepath = 'export.txt'

inFile = open(infilepath, 'r')
File = open(filepath, 'w')
line = inFile.readline()
while line:
	if (line == ('Pokemon' + '\n')):
		File.write('\n' + VRanks[r] + '\n')
		r = r + 1
		line = inFile.readline()
	else:
		linelength = line.find('\n') 
		modLine = line[:linelength]
		File.write(':' + modLine + ': ' +  modLine + '\n')
		line = inFile.readline()

print('Done. Check export.txt.')
inFile.close()
File.close()