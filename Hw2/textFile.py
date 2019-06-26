## Jason Wein
## Jan 30, 2019
## Internet Programming
## Homework 2
#Simple python program to read from a input file and print to an output file in full capitalization.
#Open a file and read the contents.
Infile = open("filein.txt","r")
text = Infile.read()
Infile.close()
lines = text.upper()
#Open a file and write the contents of "lines" to the file.
Outfile = open("fileout.txt", "w")
Outfile.write(lines)
Outfile.close()
