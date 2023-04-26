# Multiple line of text

Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output:

	
	Enter line: Beautiful is better than ugly.
	Are there more lines y/n? y
	Enter line: Explicit is better than implicit.
	Are there more lines y/n? y
	Enter line: Simple is better than complex.
	Are there more lines y/n? n 


## Program Sequence

- To start writing, open the "mylife.txt" file. The file will be generated if it doesn't exist.
- Loop until the user decides to end it.
- Request that the user enter a line of text.
- Add the text line, then a new line character, to the file.
- Ask the user if they want to enter another line of text
- Continue the loop if the users enter "y" to prompt for another line of text.
- Break the loop if the user types "n" to finish the program.
- Close the file

## Guide

- You must create a txt file in this code. However, if you forget to create the file, this program will produce it for you.

- After that, you need to run the program.

- It will prompt you to enter a line and then ask you again if you want to add more lines.

- The program will proceed if you input "y". However, typing "n" will cause the program to close.

	```
	"y" or "n"
	```

- After the running of the program, the file will be automatically closed to guarantee that all data has been written to disk.

	```
	file.close()
	```
